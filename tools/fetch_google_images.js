const google = require('googlethis');
const fs = require('fs');
const https = require('https');
const http = require('http');

const people = [
    "Rania Lampou",
    "Faisal Nabi",
    "Ismail Adaramola Abdul Azeez",
    "Chittaranjan Mandal",
    "Bhim Singh IIT Delhi",
    "Chakradhar Reddy Chandupatla",
    "R. K. Srivastava IIT BHU",
    "Anurag Jain GGSIPU",
    "Avinash Kumar Sharda University",
    "K. Meena Sharda University",
    "Henry Chima Ukwuoma",
    "Mehmet Recep Bozkurt",
    "Shriya Misra",
    "Arab Naz",
    "Qasem Abu Al-Haija",
    "Kevin M. Rivera",
    "Ilham Laabab",
    "Amit Sharma Sharda University",
    "K. Lakshmi Sharda University"
];

async function downloadImage(url, filepath) {
    return new Promise((resolve, reject) => {
        const client = url.startsWith('https') ? https : http;
        client.get(url, { headers: { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' } }, (res) => {
            if (res.statusCode === 200) {
                res.pipe(fs.createWriteStream(filepath))
                   .on('error', reject)
                   .once('close', () => resolve(filepath));
            } else {
                res.resume();
                reject(new Error(`Request Failed With a Status Code: ${res.statusCode}`));
            }
        }).on('error', reject);
    });
}

async function run() {
    for (let name of people) {
        try {
            console.log(`Searching for: ${name}`);
            const images = await google.image(`${name} face profile photo`, { safe: false });
            if (images && images.length > 0) {
                let imgUrl = images[0].url;
                
                // If it's a known bad domain or placeholder, try second one
                if (imgUrl.includes('avatar') && images.length > 1) {
                    imgUrl = images[1].url;
                }
                
                const filename = name.toLowerCase().replace(/[^a-z0-9]+/g, '-') + '.jpg';
                const path = `assets/img/people/${filename}`;
                console.log(`Downloading ${imgUrl} to ${path}`);
                try {
                    await downloadImage(imgUrl, path);
                    console.log(`Downloaded ${filename}`);
                } catch (dlError) {
                    console.log(`Failed first, trying second: ${dlError.message}`);
                    if (images.length > 1) {
                        await downloadImage(images[1].url, path);
                        console.log(`Downloaded ${filename} on second try`);
                    }
                }
            } else {
                console.log(`No images found for ${name}`);
            }
        } catch (e) {
            console.error(`Error for ${name}: ${e.message}`);
        }
    }
}

run();
