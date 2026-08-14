# Placeholders — what still needs your attention

Most of the site now carries **real Sharda University data**, sourced from
`icctdn2026.sharda.ac.in` and `sharda.ac.in` and verified where possible. This
file lists only what is still provisional, invented, or needs a human decision.

Work top to bottom — section 1 is the part that causes real harm if it goes
live wrong.

---

## 1. Must be confirmed by a human before launch

| What | Where | Why |
|---|---|---|
| **Bank account details** — ICICI a/c `025405005815`, IFSC `ICIC0007692`, SWIFT `ICICINBBCTS`, MICR `110229037`, "Sharda University — Seminar" | `registration.html` | These are carried over from the previous conference on this campus. **Confirm every field against a current document from the university finance office**, and confirm this conference is to use the same account. A red warning box sits above the table on the page — delete it once verified. |
| **Speaker names** — 9 people | `speakers.html`, `index.html` | Still carried forward from the previous edition. **Nobody should be listed as a speaker until they have agreed in writing.** The page carries a visible "carried forward, being reconfirmed" note — remove it once confirmed. The **committee is now your own confirmed list** and needs no such warning. |
| **Springer partnership** | `index.html`, `about.html#publication`, `call-for-papers.html`, `contact.html` FAQ | The site now says only that **Springer is the publication partner** — no series name, no indexing promise. Announce the series and any indexing on the About page once they are confirmed in writing. The Springer logo appears in the top bar, hero, home page and About page; remove it if the arrangement falls through. |
| **Registration fee amounts** | `registration.html` **and** the `FEES` object in `assets/js/site.js` | Modelled on the previous edition's fees. Must be approved by your organising committee. **Change both places** or the calculator will contradict the printed table. |
| **Conference dates — 18–19 December 2026** | 30+ places; `CONFIG` in `assets/js/site.js`; `data-countdown` in `index.html` | You moved the conference from 17–19 June 2027 to 18–19 December 2026. All other deadlines are derived from them (see section 3). |
| **CMT conference URL** | every page (top bar) + `call-for-papers.html` | Currently `cmt3.research.microsoft.com/ICNGCI2027/`, which does not exist yet. Create the conference in CMT and confirm the URL. |
| **Registration form URL** | `registration.html`, two "Open the registration form" buttons, currently `href="#"` | Dead links on the page people pay from. |

---

## 2. Real data now in place — no action needed

For reference, so you don't re-check these:

- **Venue address** — Plot No. 32–34, Knowledge Park III, Greater Noida, UP 201310.
- **Travel table** — all ten distances (IGIA 57 km, Hazrat Nizamuddin 36.2 km, Anand Vihar 39.6 km, Old Delhi 45.0 km, the three ISBTs, Knowledge Park II metro 3.4 km, Sharda Hospital 0.2 km) taken from the previous edition's site.
- **Nearby places** — Delhi, Vrindavan, Mathura, Kurukshetra, Haridwar, Rishikesh, with the distances as published.
- **About Sharda** — UGC approved, NAAC A+, NIRF 2023 rank 87, 63-acre campus, only multi-discipline campus in the NCR.
- **Contacts** — Dr. Subrata Sahana (subrata.sahana@sharda.ac.in, +91 93130 56608) and Prof. Sanjoy Das (sdas.jnu@gmail.com, +91 87875 38340).
- **Portraits** — 41 photographs, cropped square and optimised.
- **Track record** — five Springer and four IEEE published proceedings, with links, on `about.html#track-record`.
- **Logos** — Sharda University (with and without the NAAC badge) and Springer. Both appear in the top bar; Springer also in the publication panels; Sharda also in the footer and the About/Venue sidebars.
- **Hero image** — an aerial photograph of the Sharda campus, under a deep angled overlay so the type stays clean.
- **Springer templates** — the four official author files in `assets/downloads/`, named generically (`Springer-Word-Template.zip`, `Springer-LaTeX-Template.zip`) since the series is not fixed.

### Deliberately removed

South Asian University has been taken out entirely, per your instruction that
this is a Sharda event. That removed **three people** the previous edition
listed: Prof. K. K. Aggarwal (Chief Patron, and Guest of Honour on the speakers
page), Prof. Satya N Gupta (General Co-Chair) and Prof. S. P. Aggarwal (TPC
Co-Chair), along with their photographs. Say the word if you want any of them
restored as individuals — being at another institution does not by itself imply
co-hosting.

---

## 3. Dates — compressed to fit the new December 2026 conference

The conference moved from 17–19 June 2027 to 18–19 December 2026, which leaves
only about four months from today. The full timeline below was built from
scratch to fit that window — it is my choice, not carried over from a previous
edition, and your organising committee should sanity-check it:

| Deadline | Date | Days before conference |
|---|---|---|
| Submission portal opens | 15 August 2026 | 125 |
| Special session &amp; tutorial proposals | 15 September 2026 | 94 |
| **Full paper submission** | **1 October 2026** | **78** |
| Notification of acceptance | 25 October 2026 | 54 |
| Early-bird registration | 10 November 2026 | 38 |
| Registration &amp; camera-ready | 20 November 2026 | 28 |
| Doctoral symposium &amp; posters | 25 November 2026 | 23 |
| Slides &amp; pre-recorded video | 5 December 2026 | 13 |
| Detailed programme published | 10 December 2026 | 8 |
| Pre-conference tutorials | 17 December 2026 | 1 |
| **Conference** | **18–19 December 2026** | — |

This is a tight, compressed rhythm — about 47 days from submission portal
opening to the paper deadline, and just over three weeks for review
(submission to notification). If you want a longer review window, move the
paper deadline earlier; nothing else needs to move.

Each `<li>` in `dates.html` carries both a machine-readable `data-date` and human
text. **Change both** — the badge, the ordering and the calendar file come from
`data-date`, the visible date from the text.

---

## 4. Committee — what is filled and what is not

The committee is **your confirmed list, and only that list**. 46 named people,
plus **21 positions you left blank**, shown as *To be announced*:

| Position | Slots |
|---|---|
| Honorary Chairs | 3 (1 national, 2 international) |
| International Advisory Committee | 7 |
| National Advisory Committee | 7 |
| International Technical Program Chairs | 4 |

The **Technical Program Committee / reviewer panel** is presented as "being
formed", with a call for reviewers — the previous edition's 260-name roster has
been removed entirely.

Two entries need a decision:

- **"Kamiya"** in your Technical Program Chairs — rendered as **Kamiya Khatter, Springer**, since that is the only Kamiya in this conference's history. Correct it if that is wrong.
- **Dr. Avinash Kumar** (Track 5 chair) vs **Dr. Avinash Kumar Sharma** (Publicity Chair) — I treated them as two people, since you listed both. If they are the same person, merge them.

### Profile links and photographs

- **28 links are verified** `sharda.ac.in/faculty/details/…` faculty pages.
- **13 are Google Scholar author searches** — labelled *Scholar search*, styled grey. Replace with real URLs as you collect them.
- **36 of the 46 named people have photographs**, pulled from the Sharda faculty directory.

**Ten named people have no photograph** and show initials: Dr. Nikhil Sharma
(has one), Dr. K. Meena, Dr. Amit Sharma, Dr. Renu Mishra, Dr. K. Lakshmi,
Mr. Ashish Kumar, Dr. Gauri Shankar, Dr. Y. Suchiatra, Dr. Saptdeepa Kalita,
Dr. Sushant Jingram, Dr. Avinash Kumar — none are in the public Sharda faculty
directory under those names. Drop a square JPEG into
`assets/img/people/<name>.jpg` and swap the `person__avatar` div for an
`<img class="person__photo">`.

Two directory matches were **rejected as wrong**: "K. Lakshmi" only matches a
*S.* Lakshmi, and "Mr. Ashish Kumar" only matches a *Dr.* Ashish Kumar Chalana.

To upgrade one, find its entry in `committee.html` or `speakers.html`:

```html
<a class="person__link person__link--search" href="https://scholar.google.com/citations?view_op=search_authors&mauthors=Name">Scholar search</a>
```

and change it to:

```html
<a class="person__link" href="https://scholar.google.com/citations?user=THEIR_ID">Research profile</a>
```

(drop `person__link--search` — that class is what greys it out.)

Administrative and industry figures — the Chancellor, Pro-Chancellor, CEO, the
Springer editor, the four US-based industry speakers — deliberately have **no
link**, since a research profile is not meaningful for them. Add LinkedIn URLs
if you want them linked.



---

## 5. Still generic — write or delete

| Item | Where |
|---|---|
| Partner hotel names and negotiated rates | `venue.html#stay` — currently generic rows |
| Sponsor names in the home page logo strip | `index.html` — three empty tiles |
| Sponsorship tier amounts (`₹0,00,000`) | `contact.html#sponsorship` |
| Social media URLs (`href="#"`) | footer — set them in `index.html`, then run `python3 tools/sync-nav.py` |
| "Second Edition" in the hero eyebrow | `index.html` — change if the numbering is different |
| Programme sessions and hall names | `program.html` — provisional; hall names guessed from the campus layout |
| Speaker talk titles | `speakers.html` — the keynote titles were not published for the previous edition, so three keynote cards have no talk title |

---

## 6. Files to add — `assets/downloads/`

**The four official Springer files are already in place** — LaTeX template,
Word template, license-to-publish form and instructions for authors, pulled
from Springer's own CMS. Re-download them before the CFP opens in case Springer
revises them; keep the filenames and every link keeps working.

Four files are still yours to produce: the **Call for Papers PDF** (linked from
the top bar and footer of *every* page — add it first), the brochure, the
detailed programme, and the optional slide template. See
`assets/downloads/README.md`.

---

## 7. Policies to confirm with your committee

Drafted to current good practice, but they are commitments — read them and make
sure you will honour them.

- Double-blind review, minimum three reviewers per paper (`call-for-papers.html`)
- Similarity thresholds: 15% overall, 5% single source (`call-for-papers.html`)
- Generative-AI disclosure policy (`about.html#ethics`)
- Cancellation and refund terms (`registration.html`)
- Accessibility commitments — live captioning, sign-language interpretation on four weeks' notice, quiet room (`venue.html#access`). **Only keep what you can actually deliver.**
- Code of conduct and its reporting route (`about.html#ethics`)

---

## Pre-launch check

```bash
python3 tools/sync-nav.py --check                  # header/footer consistent
grep -rn "0,00,000\|href=\"#\"" *.html             # unfilled amounts and dead links
```

Then in a browser: click every nav item, run the fee calculator, download a
calendar file, open three profile links, and load the site on a phone.
