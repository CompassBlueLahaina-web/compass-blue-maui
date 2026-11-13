# Compass Blue at Lahaina Shores — website

Live site: https://compassbluelahaina-web.github.io/compass-blue-maui/
Owner: Kristie. Hosted free on GitHub Pages. Plain HTML and CSS: no framework, no build step, no paid services, no JavaScript except the owner's Google Analytics tag.

## Rules for anyone (person or AI) editing this site

1. **Exact name, everywhere:** "Compass Blue at Lahaina Shores". Never "Compass Blue" alone in a title or heading; it collides with the Compass real estate brokerage in search. Pair it with Lahaina Shores or 475 Front Street.
2. **Never invent facts** (review counts, distances, rates, views). If it is not in the table below, ask Kristie.
3. **No new subscriptions or accounts** without asking Kristie first. Prefer free or one-time options.
4. Keep it plain HTML/CSS so the folder can be moved to any web host as-is.

## Agreed facts (decided by Kristie, November 2026)

| Topic | Use this | Do not use |
|---|---|---|
| Name | Compass Blue at Lahaina Shores | Compass Blue Lahaina, Compass Blue Maui, King's View |
| Address | 475 Front Street, Lahaina, HI 96761 | |
| Area label | "Kaanapali area of West Maui" alongside the Lahaina address (Kristie's choice) | "Kaanapali Beach" or anything implying the studio is at the Kaanapali resorts (they are 5 miles north) |
| View | Lanai faces the West Maui Mountains. Building is oceanfront/beachfront. | "ocean view" for the studio or lanai; whales "from the lanai" |
| Whales | Seen from the beach in front of the building, Nov–May, peak Jan–Mar | |
| Beachfront claim | "an oceanfront building", "beach steps from the lobby". About the building (not the unit): "the only resort on this stretch of beach, so the sand stays uncrowded" (Kristie, 13 Nov 2026) | "the only beachfront rental" (other units in the building are beachfront too); "for miles" or crowd numbers, which cannot be checked |
| Harbor / Banyan Tree | 2 to 3 blocks | "2 blocks" |
| ʻUlu o Lele Marketplace | about a mile | "a block" |
| Reviews | Quote real reviews; link to live listings. No totals. | "460+ reviews", "22 reviews", "Top 5%" |
| Sleeps | 3 (queen + two convertible twin chairs) | 4 |
| Parking | Resort lot $15/day, or free on Shaw Street | "parking included" |
| Surf lessons | Hi Surf Club and pop-up board rentals next door | Bully's (older wording) |
| Group size | Sleeps 3 at most; most comfortable for 1 or 2 | |
| Monk seals | "about 1,600 remain (NOAA)" | "fewer than 1,300" |
| Rates | Do not print nightly rates or competitor prices | |

## Files

| File | What it is |
|---|---|
| `index.html` | Home page: studio, beach, location, reviews, booking |
| `guide.html` | Guest guide |
| `faq.html` | Questions and answers |
| `assets/css/style.css` | All styling. Colors and fonts are at the top under `:root` |
| `assets/img/` | Photos. Each has `name-640.webp`, `name-1280.webp` and `name.jpg` |
| `assets/fonts/` | Young Serif and Figtree (free, SIL Open Font License), stored here so nothing loads from Google |
| `llms.txt` | Plain-text fact sheet for AI assistants. Keep in step with the table above |
| `sitemap.xml`, `robots.txt` | For search engines. Update `lastmod` dates in the sitemap when pages change |
| `404.html` | Shown for broken links |
| `google265fb90a562fd6f2.html` | Google Search Console ownership proof. Do not delete |
| `listing-copy/airbnb.md` | The agreed Airbnb listing text, so the site and the listing stay consistent |
| `tools/` | Optional helper scripts; see Status and handoff |
| `private-bathroom.jpg` | Old photo kept only so old links to it do not break |

The header and footer are repeated in each of the three pages. Change them in all three.
In `faq.html` each question appears twice: once as visible text and once in the `application/ld+json` block near the top (that block is what search engines and AI read). Change both.
`index.html` also has an `application/ld+json` block describing the rental; keep it in step with the visible text.

## Changing something small (no tools needed)

1. Go to the repository on github.com and click the file (for example `index.html`).
2. Click the pencil icon, change the words, click **Commit changes**.
3. The live site updates in a minute or two. Every change is saved in **History** and can be undone.

## Adding or replacing a photo

Give the original photo to Claude and ask for "640 and 1280 wide WebP plus a JPG, location data removed, into assets/img". Never publish a photo showing the unit number, door code, WiFi details or a QR code.

## Backup

- **Site:** on the repository page click the green **Code** button, then **Download ZIP**. Save it somewhere safe (computer plus a cloud drive). Do this after any change.
- **Photos:** keep your original photo files; the site only holds shrunken copies.
- **Reviews:** platforms own the review pages, so keep your own copy. Airbnb: Account > Privacy > Request your personal data sends a file that includes reviews. VRBO and Houfy: open the reviews page and use the browser's Print > Save as PDF every few months.

## Booking and contact (decided by Kristie, November 2026)

- The booking path is Houfy (direct, no guest service fee), with Airbnb and VRBO as alternatives. Guests message through whichever they use.
- **No request forms and no "email us" or "text us" buttons.** Do not add them.
- The phone number and email stay in the footer, `llms.txt` and the structured data only, because site-quality checkers and AI crawlers flag a business page with no contact details as incomplete.
- Boat tours: do not list operators by harbor. Tell guests to check the departure point (Lahaina Harbor is walkable; Mala Wharf, Māʻalaea Harbor and Kaanapali Beach are not).

## Status and handoff (last updated 13 November 2026)

Any Claude model (or person) can pick this up from this file alone.

**Done:** accuracy fixes, single name, new design, FAQ page, guest guide, structured data, sitemap, `llms.txt`, Kristie's own photos, booking limited to Houfy/Airbnb/VRBO.

**How Kristie publishes:** she has no GitHub link to Claude. Claude hands her a zip of the whole site folder; she unzips it and drags the contents onto **Add file > Upload files** on github.com, then **Commit changes**. Explain every step in plain language.

**Waiting on Kristie:**
- YouTube video links to embed (she made the videos; use `youtube-nocookie.com`, `loading="lazy"`).
- Better photos (see below).
- Where the underwater turtle photo was taken (its caption names no beach).
- Aligning her Houfy, Airbnb and VRBO titles to the exact name (she does this herself; never change platform settings for her).

**Photos: what Kristie likes and dislikes**
- The bed is now dressed in all white with **no throw pillows** (guests find them unhygienic). Do not lead with any photo showing a rumpled bed or decorative pillows on the bed. The old "bed-mountains" photo was removed for this reason.
- Dark, backlit phone shots look poor next to the brighter ones. Crop to the bright part and lift shadows gently. Colour correction is fine; never add, remove or invent objects or scenery.
- Lead photo is `room-orchid` (white bed, lanai behind). The mountain panel uses `lanai-mountains`, cropped and brightened from her original.
- `from-the-water` (building from the ocean, mountains behind) is the wide photo in the location section and the social-share image. It is by her father, Bill Halsey, and is credited to him in the caption; keep the credit. `turtle-beach` was taken in front of Lahaina Shores (building visible).
- She shared an aerial drone photo for context only. It is not hers and must not be used.
- Remaining weak spots: `room-lanai` and `room-orchid` still show a throw pillow on the armchairs; `bed-lanai` is small (960 px). Replace when she sends new ones.
- Shot list to ask for: (1) freshly made all-white bed with the mountains through the doors, shot mid-morning with lights on; (2) the lanai from inside the doorway on a clear day; (3) a rainbow over the mountains; (4) the beach in front of the building.

**Location map:** the map in the location section of `index.html` is a hand-drawn SVG (no map service, no tracking, nothing to pay for). It is simplified and not to scale, drawn from Apple Maps screenshots Kristie supplied. To add a place, copy one of the `<a>…</a>` pin groups and change its position and text. It deliberately shows roads and landmarks only, not satellite imagery.

**Tone and positioning (Kristie, 13 Nov 2026):** the guest she wants is comparing her with the Kaanapali resorts, not with cheaper units in her building. Sell the positives: uncrowded beach, the only resort on this stretch of sand, same coastline as Kaanapali, full kitchen, far lower cost than the resorts, local vendors at ʻUlu o Lele. She does not compete on low price and does not want advice to cut rates. The 2023 fire is not mentioned on the home page, guide or Airbnb text; the only place it appears is the FAQ question "Is Lahaina open to visitors after the 2023 fire?", kept because people search for it. Do not print her costs, rates or fee settings in this public repository.

**`tools/` folder:** the small Python scripts Claude used to write the three pages and shrink photos (`python3 tools/mk_index.py .` etc., needs Pillow). They are a convenience, not a requirement: the `.html` files are complete on their own and can be edited by hand. If you edit a page by hand, the matching script is out of date; either update it too or delete `tools/`.

## Ideas not built

- **Availability display (free):** a Google Calendar subscribed to the Airbnb calendar export link, set to show only "busy", embedded on the page. It can lag by up to a day. Houfy already shows the live calendar, so this is optional.
- **Videos:** embed Kristie's YouTube videos with `youtube-nocookie.com` and `loading="lazy"` so they do not slow the page.
- **Direct bookings and tax:** if payment is ever taken outside Houfy/Airbnb/VRBO, the owner collects and remits Hawaii taxes herself. Confirm with an accountant first. Not tax advice.
