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
| Beachfront claim | "an oceanfront building", "beach steps from the lobby" | "the only beachfront rental" |
| Harbor / Banyan Tree | 2 to 3 blocks | "2 blocks" |
| ʻUlu o Lele Marketplace | about a mile (a mile or less); walkable | "a block" |
| Cannery / Keawe Hub area | about three blocks farther than ʻUlu o Lele, a little over a mile from the studio (Kristie, November 2026) | "a couple of blocks from ʻUlu o Lele" |
| Other walking distances | Give the distance, not "easy walk"; ability and opinion vary | |
| Reviews | Quote real reviews; link to live listings. No totals. | "460+ reviews", "22 reviews", "Top 5%" |
| Sleeps | 3 (queen + two convertible twin chairs) | 4 |
| Parking | Resort lot $15/day, or free on Shaw Street | "parking included" |
| Monk seals | "about 1,600 remain (NOAA)" | "fewer than 1,300" |
| Rates | Do not print nightly rates or competitor prices | |
| Hosting experience | "more than 20 years of hosting, 13 of them on Airbnb" (Kristie, November 2026) | "13 years" alone |
| Houfy vs Airbnb/VRBO price | "no guest service fee" and "the total for your dates is usually lower" (Kristie's statement, November 2026). Airbnb may build its fee into the nightly rate, so do not say Airbnb "adds" a fee | "skip the service fees Airbnb and VRBO add" |

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
| `private-bathroom.jpg` | Old photo kept only so old links to it do not break |

The header and footer are repeated in each of the three pages. Change them in all three.
In `faq.html` each question appears twice: once as visible text and once in the `application/ld+json` block near the top (that block is what search engines and AI read). Change both.
`index.html` also has an `application/ld+json` block describing the rental; keep it in step with the visible text.

## Publishing a new version of the whole site

1. Unzip the site folder on your computer.
2. On the repository page on github.com click **Add file > Upload files**.
3. Open the unzipped folder and drag its **contents** (index.html, faq.html, guide.html, assets, and the rest) into the page. Do not drag the folder itself, or the files end up one level too deep and the site breaks.
4. Type a short note such as "Site update" and click **Commit changes**. The live site updates in a minute or two, and **History** keeps the old version.
5. Afterward, resubmit sitemap.xml in Google Search Console and Bing Webmaster Tools.

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

## Ideas not built

- **Availability display (free):** a Google Calendar subscribed to the Airbnb calendar export link, set to show only "busy", embedded on the page. It can lag by up to a day. Houfy already shows the live calendar, so this is optional.
- **Videos:** embed Kristie's YouTube videos with `youtube-nocookie.com` and `loading="lazy"` so they do not slow the page.
- **Direct bookings and tax:** if payment is ever taken outside Houfy/Airbnb/VRBO, the owner collects and remits Hawaii taxes herself. Confirm with an accountant first. Not tax advice.
