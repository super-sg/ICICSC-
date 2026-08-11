const puppeteer = require('puppeteer');
const fs = require('fs');
const https = require('https');
const http = require('http');

const html = fs.readFileSync('committee.html', 'utf-8');

// Regex to find people with avatars and scholar links
const personRegex = /<div class="person">[\s\S]*?<div class="person__avatar"[^>]*>.*?<\/div>[\s\S]*?<p class="person__name[^>]*>([^<]+)<\/p>[\s\S]*?<a class="person__link" href="https:\/\/scholar\.google\.[^/]+\/citations\?[^"]*user=([^"&]+)[^"]*"/g;

async function downloadImage(url, filepath) {
    return new Promise((resolve, reject) => {
        const client = url.startsWith('https') ? https : http;
        client.get(url, { headers: { 'User-Agent': 'Mozilla/5.0' } }, (res) => {
            if (res.statusCode === 200) {
                res.pipe(fs.createWriteStream(filepath))
                   .on('error', reject)
                   .once('close', () => resolve(filepath));
            } else {
                res.resume();
                reject(new Error(`Status Code: ${res.statusCode}`));
            }
        }).on('error', reject);
    });
}

function generateSlug(name) {
    let clean = name.replace(/\b(Dr\.|Prof\.|Mr\.|Ms\.|Er\.|Dr|Prof|PhD|Ph\.D)\b/gi, '')
                    .replace('(Dr.)', '').replace(/[(),]/g, '');
    clean = clean.replace(/IIT Delhi|IIT BHU|GGSIPU|Sharda University/g, '');
    return clean.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
}

async function scrapeScholar() {
    let match;
    const targets = [];
    
    // Some links use h=en&user=XYZ instead of user=XYZ&hl=en, we need a better regex or HTML parsing.
    // Let's use a simpler approach: Just run through all missing people and use Puppeteer.
    
    console.log("Starting Puppeteer...");
    const browser = await puppeteer.launch({ headless: "new", args: ['--no-sandbox'] });
    const page = await browser.newPage();
    await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36');

    // To parse properly, let's use a simple regex to get all missing people and their blocks
    const blockRegex = /<div class="person">([\s\S]*?)<\/div>\s*<\/div>/g;
    
    let blocks = [...html.matchAll(/<div class="person">([\s\S]*?)<\/a>\s*<\/div>\s*<\/div>/g)];
    
    for (let b of blocks) {
        const block = b[1];
        if (block.includes('class="person__avatar"')) {
            const nameMatch = block.match(/<p class="person__name[^>]*>([^<]+)<\/p>/);
            const scholarMatch = block.match(/href="(https:\/\/scholar\.google\.[^"]+)"/);
            
            if (nameMatch && scholarMatch) {
                const name = nameMatch[1].trim();
                const scholarUrl = scholarMatch[1];
                let slug = generateSlug(name);
                
                // Edge cases
                if (slug === 'henry-chima-chima-ukwuoma') slug = 'henry-chima-ukwuoma';
                
                console.log(`\nChecking ${name} (${scholarUrl})`);
                
                try {
                    await page.goto(scholarUrl.replace(/&amp;/g, '&'), { waitUntil: 'domcontentloaded', timeout: 15000 });
                    // Wait a bit to act human
                    await new Promise(r => setTimeout(r, 2000));
                    
                    const imgUrl = await page.evaluate(() => {
                        const img = document.querySelector('#gsc_prf_pup-img');
                        return img ? img.src : null;
                    });
                    
                    if (imgUrl) {
                        if (imgUrl.includes('avatar_scholar')) {
                            console.log(`-> ${name} has default avatar on Scholar. Skipping.`);
                        } else {
                            console.log(`-> Found image URL: ${imgUrl}`);
                            const path = `assets/img/people/${slug}.jpg`;
                            await downloadImage(imgUrl, path);
                            console.log(`-> Saved to ${path}`);
                        }
                    } else {
                        console.log(`-> Could not find image element on page.`);
                    }
                } catch (err) {
                    console.log(`-> Error visiting page: ${err.message}`);
                }
            }
        }
    }
    
    await browser.close();
    console.log("Done.");
}

scrapeScholar();
