# ICICSC 2027 — Conference Website

Static website for the **International Conference on Intelligent, Connected and Sustainable Computing (ICICSC 2027)**, 28–29 May 2027, hosted by the Sharda School of Computing Science & Engineering, **Sharda University, Greater Noida**.

Plain HTML5, CSS3, and vanilla modern JavaScript. **No build step, zero dependencies.** Deployable out of the box to Vercel, Netlify, Cloudflare Pages, or GitHub Pages.

---

## Deployment on Vercel

This repository is pre-configured for Vercel deployment with [vercel.json](file:///Users/supersg/Documents/Random%20Projects/Conference%20SIte%20%28IEEE%29/vercel.json):
1. Push to GitHub (`git push origin main`)
2. Import project in **Vercel Dashboard**
3. Select **Other / Plain HTML** (no build command or output directory needed)
4. Click **Deploy**

---

## Running Locally

```bash
python3 -m http.server 8080
# then open http://localhost:8080
```

---

## Site Structure

```
index.html              Home — hero, countdown, tickers, tracks, dates, fees, venue
about.html              About, objectives, publication policy, host, awards, ethics
tracks.html             All 7 tracks with SDG alignment, searchable and filterable
call-for-papers.html    CFP, submission categories, manuscript prep, plagiarism policy
dates.html              Full author timeline with live status + calendar downloads
registration.html       Fee tables, fee calculator, payment details, policies, FAQ
committee.html          Chief Patrons, Patrons, Honorary Chairs, Advisory Board, TPC, Organizing
speakers.html           Distinguished Keynote Speakers
program.html            Day-by-day programme schedule, presentation guidelines
venue.html              Address, map, travel, accommodation, visa, attractions, access
contact.html            Contact routing, secretariat, enquiry form, sponsorship, FAQ
404.html                Not-found page

assets/css/main.css     Bespoke vanilla CSS design system
assets/js/site.js       All interactions, countdowns, fee calculators, filter systems
assets/img/flags/       SVG Country Flags
assets/img/logos/       University & Institution crests / logos
assets/img/people/      Speaker & Committee portraits
assets/downloads/       Templates & guidelines
robots.txt, sitemap.xml SEO metadata
```
