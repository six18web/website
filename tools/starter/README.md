# Six18 Web Starter Site template

One-page, phone-first client website built from a JSON config. Used for the $950 Starter Site.

## Make a new client site

1. Copy `config.example.json` to a new file named for the client, and fill in every value.
   Use real reviews only, with the customer's permission.
2. Put the client's photos and logo in the output folder (for example `photos/job1.jpg`) and list them
   in `photos`, `hero_photo`, and `logo`. Give every photo a plain description in `alt`.
3. Build it:

   ```
   python3 tools/starter/starter.py clients/acme-roofing.json ../acme-roofing-site
   ```

4. Open `index.html` in a browser, check it on a phone, and send the client a preview.
5. Publish: put the output folder in its own GitHub repo (or the client's host), point the client's
   domain at it, and submit `sitemap.xml` in Google Search Console.

## What every site gets

- Tap-to-call in the header and a sticky Call / Quote bar on phones
- Page title and description that name the trade and town
- LocalBusiness structured data (set `schema_type`, e.g. `RoofingContractor`, `Plumber`,
  `HairSalon`, `AutoRepair`, `Restaurant`)
- Services, about, photos, reviews, service area with map, hours, and a contact form
- Contact form: `"kind": "mailto"` opens the visitor's email app; for a Google Form, set
  `"kind": "google"`, the form's `formResponse` URL, and the field entry IDs
  (`f-name`, `f-phone`, `f-email`, `f-svc`, `f-msg`), the same way six18web.com does it
- Home address hidden unless `show_address` is true
