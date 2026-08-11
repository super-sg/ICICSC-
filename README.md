# ICNGCI 2026 — conference website

Static website for the **International Conference on Next-Generation Computing
and Innovations**, 18–19 December 2026, hosted by the Sharda School of Computing
Science & Engineering, **Sharda University, Greater Noida**.

Plain HTML, CSS and vanilla JavaScript. **No build step, no framework, no
dependencies.** Copy the folder onto any web server — a university host, cPanel,
Netlify, GitHub Pages, an S3 bucket — and it works. That is deliberate: a
conference site has to outlive whoever built it, and be editable by whoever
inherits it three years from now.

---

## Before you publish: read `PLACEHOLDERS.md`

Every value that must be replaced — university name, dates, emails, bank
account, submission portal URL — is listed there with the exact file and line.
**The bank details in particular must not go live as-is.**

---

## Running it locally

```bash
cd "ICNGCI Conference Site"
python3 -m http.server 8000
# then open http://localhost:8000
```

Opening `index.html` directly with `file://` mostly works, but the calendar
downloads and the map embed behave better over HTTP. Use the server.

---

## What is here

```
index.html              Home — hero, countdown, tracks, dates, fees, venue
about.html              About, objectives, publication policy, host, awards, ethics
tracks.html             All 6 tracks / 90 topics, searchable and filterable
call-for-papers.html    CFP, submission categories, manuscript prep, plagiarism policy
dates.html              Full author timeline with live status + calendar downloads
registration.html       Fee tables, fee calculator, payment details, policies, FAQ
committee.html          Patrons, advisory, TPC + call for reviewers, organizing
speakers.html           Keynotes, industry and invited talks, speaker proposals
program.html            Day-by-day programme, presentation guidelines
venue.html              Address, map, travel, accommodation, visa, attractions, access
contact.html            Contact routing, secretariat, enquiry form, sponsorship, FAQ
404.html                Not-found page

assets/css/main.css     The entire design system (one file, sectioned + commented)
assets/js/site.js       All behaviour (one file, one module per feature)
assets/img/             hero.jpg (campus), favicon.svg
assets/img/people/      55 committee and speaker portraits, 520x520, optimised
assets/img/logos/       Sharda University (colour + white), Springer
assets/downloads/       Official Springer templates + README of what to add
tools/sync-nav.py       Propagates header/footer edits from index.html to all pages
robots.txt, sitemap.xml SEO — update the domain in both
```

---

## How to make common changes

### Change the conference dates

The current dates are spaced to match the previous edition hosted on this campus
— see the table in `PLACEHOLDERS.md`. To move them, three places:

1. **`assets/js/site.js`** — the `CONFIG` block at the very top. This drives the
   countdown and every "Add to calendar" file.
2. **The visible text** — search and replace `18–19 December 2026` across the
   `.html` files (note the en dash `–`, not a hyphen).
3. **`index.html`** — the `data-countdown="2026-12-18"` attribute on the
   countdown list.

### Change a deadline

Edit the `<li>` in `dates.html` (and the shortened list on `index.html`). Each
one looks like:

```html
<li data-date="2026-09-15" data-title="Full paper submission deadline">
  <span class="dates__label">Full paper submission deadline</span>
  <span class="dates__meta"><span class="dates__when">15 September 2026</span></span>
</li>
```

`data-date` is what the code reads — it computes the *Closed / Today / N days
left / Upcoming* badge automatically and generates the calendar file. The text
inside `dates__when` is what humans see. **Keep the two in sync.** Add
`data-end="2026-12-19"` for a multi-day event.

### Change registration fees

Two places, and both matter:

1. The tables in `registration.html` (what people read).
2. The `FEES` object in `assets/js/site.js` → `initFeeCalc()` (what the
   calculator computes). If these disagree, delegates will trust the calculator
   and then dispute the invoice.

### Add or rename a menu item

Edit the `<nav class="mainnav">` block in **`index.html` only**, then run:

```bash
python3 tools/sync-nav.py
```

That copies the header and footer from `index.html` into all other pages. Run
`python3 tools/sync-nav.py --check` in CI or before committing to confirm
nothing has drifted. The active-page highlight is derived from the URL at
runtime, so the nav markup stays byte-identical everywhere — no per-page edits.

### Add a track or topic

`tracks.html` — copy an `<article class="track">` block, bump the number, and
set `data-track="7"` and `style="--tc:var(--t1)"` (or define a `--t7` colour in
`main.css` under *Tokens*). The search and filter pick it up with no JS change;
add a matching `<button class="chip" data-track-filter="7">` to the toolbar.

### Add or replace a person

Portraits live in `assets/img/people/<name>.jpg`, prepared as **520×520
squares**. The CSS assumes square sources: the small card shows the square
whole, and the large speaker card trims it to 4:3 anchored 20% from the top so
the head stays clear of the edge. Feed it a non-square image and it will crop
badly.

To prepare one:

```python
from PIL import Image, ImageOps
im = ImageOps.exif_transpose(Image.open("photo.jpg")).convert("RGB")
w, h = im.size; s = min(w, h)
im = im.crop((0, int((h-s)*0.12), s, int((h-s)*0.12)+s)) if h > w else im.crop(((w-s)//2, 0, (w-s)//2+s, s))
im.resize((520, 520), Image.LANCZOS).save("assets/img/people/name.jpg", quality=82, optimize=True)
```

Four committee members have no photograph and fall back to initials — that is a
designed state, not a bug. See `PLACEHOLDERS.md` §4.

### Change a profile link

Each person links to a research profile. Grey *Scholar search* links are name
searches, not confirmed profiles — `PLACEHOLDERS.md` §4 explains how to upgrade
them.

### Change the colours

`assets/css/main.css`, section 1 (*Tokens*). `--primary` and `--accent` drive
buttons and links; `--t1` … `--t6` colour-code the tracks. Everything else
derives from those.

---

## Design notes

The visual language is adapted from the **MIT Department of Chemistry** site:
Roboto throughout with heavy display weights (900) at tight negative tracking,
squared geometry with no rounded corners, a white canvas with generous
whitespace, and saturated multi-hue accents used sparingly against near-black.
Section headers use a title on the left with a link on the right above a 2px
rule; content sits in bordered cards on a `#f4f4f4` band.

The content model is taken from the previous conference hosted on this campus —
countdown, publishing and indexing block, important dates, downloadable CFP,
deep committee structure, venue with transport table and nearby attractions,
registration with bank details — reorganised so the four things authors
actually come for (**deadline, tracks, how to submit, what it costs**) are each
one click from any page.

### Accessibility and robustness

- Skip link, landmark elements, and a visible focus ring on every interactive element.
- Tabs implement the ARIA tab pattern with arrow-key navigation; dropdowns work by hover, click and keyboard, and close on `Escape`.
- All content is real HTML — the pages read correctly with JavaScript disabled. JS only adds behaviour (countdown, filters, calculator, calendar files), never content.
- Colour is never the only signal: deadline status has a text badge, not just a strike-through.
- `prefers-reduced-motion` is honoured.
- Print stylesheet strips navigation and expands link URLs, so the CFP and programme print cleanly.
- No page scrolls horizontally at any width; wide tables scroll inside their own container.

### Privacy

There is **no analytics, no tracking, no third-party JavaScript, and no
cookies**. The only external requests are Google Fonts (Roboto) and the Google
Maps iframe on `venue.html`. If your institution requires zero third-party
requests, self-host Roboto and replace the map with a static image plus a link —
nothing else needs to change.

The contact form composes a `mailto:` draft in the visitor's own mail client.
No data is transmitted to or stored on the server. If you want a real form
backend, replace the `<form id="contact-form">` action with your endpoint and
delete the handler in `initMisc()`.

---

## Deployment

Upload the whole folder. Set `index.html` as the default document. Two things to
check afterwards:

- Update the domain in `robots.txt`, `sitemap.xml`, and the `<link rel="canonical">` in `index.html`.
- The site assumes it is served from the **domain root**. If you deploy into a
  subdirectory (e.g. a GitHub Pages project site at `/icngci/`), the relative
  links still work, but `404.html` will not find its stylesheet. Either deploy
  at the root, or use a custom domain.

Enable HTTPS. A conference site that asks for bank transfers over plain HTTP
will — correctly — be distrusted.

---

## The Word document

`assets/downloads/ICNGCI-2026-Conference-Information.docx` holds the complete
content of the site — about, all 6 tracks and 90 topics, call for papers,
important dates, submission guidelines, fee tables, the full committee
including the 260-member TPC roster, speakers, programme, venue and contacts.
About 8,600 words across 36 tables.

It is **generated from the HTML**, not maintained separately, so the two cannot
drift apart. After editing any page:

```bash
./tools/make-docx.sh
```

First run creates `tools/.venv` and installs `python-docx` (its only
dependency, kept out of your system Python). The venv is gitignored.

---

## Deploying to Vercel

The repo is at <https://github.com/super-sg/ICNGCI-Conference-SIte>.

**Dashboard (recommended)** — gives you a redeploy on every `git push`:

1. <https://vercel.com/new> → **Import Git Repository** → pick `ICNGCI-Conference-SIte`.
2. Framework Preset: **Other**. Leave Build Command, Output Directory and
   Install Command **empty** — this is a static site with no build step.
3. **Deploy.**

**CLI**, if you prefer:

```bash
npx vercel login
npx vercel --prod
```

`vercel.json` is already in the repo: long cache on images, short
must-revalidate cache on CSS/JS (there is no content hashing, so a long cache
there would strand visitors on stale styles), and standard security headers.
`404.html` is picked up automatically.

After the first deploy, update the domain in `robots.txt`, `sitemap.xml` and
the `<link rel="canonical">` in `index.html`.
