# Images

## `hero.jpg` — the home page banner

Drop a photograph here named exactly **`hero.jpg`** and it appears behind the
home page hero automatically. No CSS change is needed.

* Recommended: **2400 × 1350 px** or larger, landscape, under 400 KB after
  compression (use [squoosh.app](https://squoosh.app) or `cwebp`).
* Pick something with a **calm upper-left region** — the headline sits there.
  A wide campus shot, a laboratory, or an auditorium during a talk all work.
* The stylesheet lays a dark blue/magenta gradient over the image, so a photo
  that is slightly too bright or too busy will still read well. A photo with a
  lot of fine detail and high contrast will not.
* **Use a photo you have the right to publish.** Campus photographs taken by
  your own communications office are the safest choice. If you use a stock
  image, keep the licence on file.

If no `hero.jpg` is present, the hero falls back to the gradient alone, which
is a deliberate, finished-looking design — the site does not look broken
without it.

## `favicon.svg`

The browser-tab icon. Replace with your university mark if you have an SVG
version; keep the filename, or update the `<link rel="icon">` tag in all
twelve HTML files.

## Other images you may want to add

| File | Used for | Suggested size |
|---|---|---|
| `og-image.jpg` | Link preview on social media and WhatsApp | 1200 × 630 px |
| `speakers/*.jpg` | Speaker portraits on `speakers.html` | 600 × 600 px, square |
| `logos/*.svg` | Sponsor and partner logos in the home page logo strip | SVG preferred |

To use a speaker portrait, replace the `<div class="person__avatar">TBA</div>`
block in `speakers.html` with:

```html
<img class="person__avatar" src="assets/img/speakers/name.jpg" alt="" style="height:170px;object-fit:cover">
```
