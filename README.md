# GRAIN Bootstrap holding website

This folder contains an eight-page static website and an upload-ready ZIP. It is a temporary public site while the full Next.js platform is planned. The ZIP contains the contents of `site/` at its root, so `index.html` will land directly in the hosting document root after extraction.

The website's main green theme is `#005252` in the styles and browser theme color. The original dark and light GRAIN logo SVGs are used without color changes. Light supporting surfaces use neutral tones for readable contrast. The supplied photographs and event posters remain unedited. `site/index2.html` is an alternate homepage design; `site/index.html` remains the default homepage.

## Upload

1. Back up the current hosting document root.
2. Upload `brain-bootstrap-website.zip` to the GRAIN hosting account.
3. Extract the ZIP **inside the document root** (often `public_html`). Confirm that `index.html` is directly in that root, alongside `contact.html`, `assets/`, and the other HTML files.
4. Open the live home page and all navigation links over HTTPS. Check the mobile menu, images, event detail pages, and `mailto:`/`tel:` links.
5. Clear any hosting or CDN cache if older files persist.

No Node.js, PHP, database, build step, or server rewrite rule is required for the uploaded site. Bootstrap and Bootstrap Icons are loaded from jsDelivr, and the two web fonts are loaded from Google Fonts. The custom styling and behavior are in `site/assets/css/styles.css` and `site/assets/js/site.js`.

## Show the home page without `index.html`

Keep `index.html` in `public_html`: the web server uses it to serve `https://grainglobal.org/`. The site's Home, logo, footer, and breadcrumb links point to `./`, so they open the clean root URL. Upload the refreshed HTML files from this ZIP to apply that change to the live site.

To make an old or manually entered `https://grainglobal.org/index.html` URL redirect to `https://grainglobal.org/`, add the following near the top of the existing `public_html/.htaccess` file on an Apache or LiteSpeed cPanel server. Enable **Show Hidden Files** in cPanel File Manager first. Preserve any existing rules; do not replace the file. If `.htaccess` does not exist, create it in `public_html`.

```apache
RewriteEngine On
RewriteCond %{THE_REQUEST} \s/+index\.html[?\s] [NC]
RewriteRule ^index\.html$ / [R=301,L]
```

Visit `/` first to confirm the home page works, then visit `/index.html` to check that the address changes to `/`. A 301 redirect may be cached by browsers, so test in a private window if needed. These instructions apply only when this site is deployed at the domain root.

## Pages

- `index.html` — Home
- `index2.html` — alternate Home design with a full-image hero and side menu
- `our-organization.html` — Our Organization
- `events.html` — Events
- `news.html` — News & Updates
- `contact.html` — Contact Us
- `event-startup-summit.html`, `event-grasag-congress.html` — event details
- `news-direction.html` — strategy note

## Contact behavior

The displayed email is `info@grainglobal.org`, and the phone number is `(+233) 123-456-7890`, as supplied for this task. The contact form opens the visitor's own email application with a prepared message. It **does not send, store, or process** a message on the hosting server. The visitor must press Send in their email application. Direct email and phone links remain available if the form cannot open an email application.

To change contact details throughout the site, edit the displayed details in the HTML and keep the generator constants in sync. The generator is older than the current hand-edited pages: running it overwrites the eight standard HTML pages, including FAQ and responsive design changes. Update the generator first, or review its output with `git diff` before accepting any regenerated pages. It does not generate `index2.html`.

## Git workflow

The repository root is this folder. Website files live in `site/`; the generator and this README are kept alongside them. `.gitignore` excludes macOS metadata, Python cache, and the packaged upload ZIP.

Make changes locally, review them in a browser, and inspect `git diff`. Commit and push a reviewed change when it is approved. A commit alone does not deploy the website to its hosting account.

## Source and publication review

The copy follows `Documents/GRAIN GCC Strategic Direction and Action Plan 2026-2027. v1.docx`. The reference PPTX has different vision, mission and tagline wording, so the official language should be confirmed. The summit and congress information comes from supplied posters and selected photographs. Confirm event attribution, image-use permission, titles and captions before public upload. Stock photographs are marked as illustrative in alt text; verify their license for website use. No office address, chapter roster, membership portal, RIC Bank link, or unverified impact figures have been added.

The Bootstrap design is original code informed by the supplied benchmark screenshots. It does not include the Workforce theme's code, assets, dummy contact details, or sample metrics.

## Regenerate and package

From this folder:

```sh
python3 generate_site.py
cd site
zip -r -X ../brain-bootstrap-website.zip . -x '*.DS_Store' '__MACOSX/*'
```

Check the ZIP contents with `unzip -l brain-bootstrap-website.zip` before uploading. If a page looks unstyled on the server, verify that external CDNs are reachable and `assets/css/styles.css` is present at the expected path.
