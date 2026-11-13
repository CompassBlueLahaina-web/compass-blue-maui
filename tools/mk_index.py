import sys
from common import *
biz = {
 "@context":"https://schema.org","@type":"LodgingBusiness","@id":BASE+"#rental",
 "name":NAME,"alternateName":["Compass Blue Lahaina Shores","Compass Blue, 475 Front Street, Lahaina"],
 "description":"Owner-hosted studio vacation rental inside Lahaina Shores Beach Resort, an oceanfront building at 475 Front Street, Lahaina, in the Kaanapali area of West Maui. Sleeps 3 with a queen bed and two convertible twin beds, a full kitchen, a private bathroom with solid doors, and a lanai that faces the West Maui Mountains. The beach is steps from the lobby. Lahaina Harbor and the Lahaina Banyan Tree are 2 to 3 blocks away. Not affiliated with Compass real estate.",
 "url":BASE,"telephone":"+1-808-667-7088","email":"CompassBlueLahaina@gmail.com",
 "address":{"@type":"PostalAddress","streetAddress":"475 Front Street","addressLocality":"Lahaina","addressRegion":"HI","postalCode":"96761","addressCountry":"US"},
 "geo":{"@type":"GeoCoordinates","latitude":20.8672,"longitude":-156.6751},
 "containedInPlace":{"@type":"Resort","name":"Lahaina Shores Beach Resort","address":"475 Front Street, Lahaina, HI 96761"},
 "image":[BASE+"assets/img/"+n+".jpg" for n in ["from-the-water","room-orchid","room-lanai","lanai-mountains","kitchen","bathroom","pool-day","lobby-ocean"]],
 "numberOfRooms":1,"occupancy":{"@type":"QuantitativeValue","maxValue":3},
 "petsAllowed":False,"checkinTime":"15:00","checkoutTime":"11:00",
 "amenityFeature":[{"@type":"LocationFeatureSpecification","name":n,"value":True} for n in [
   "Oceanfront building with direct beach access","The only resort on its stretch of beach","Lanai with West Maui Mountain view","Full kitchen","Private bathroom with solid doors","Queen bed and two convertible twin beds","Central air conditioning","Free WiFi","Shared oceanfront pool and hot tub","Bakery cafe in the lobby","Walk to Lahaina Harbor and the Lahaina Banyan Tree"]],
 "identifier":[{"@type":"PropertyValue","name":"Hawaii TAT ID","value":"TA-099-540-7360-01R"},{"@type":"PropertyValue","name":"Hawaii GET ID","value":"GE-099-540-7360-01R"},{"@type":"PropertyValue","name":"TMK","value":"4-6-002-007-0070"}],
 "sameAs":[AIRBNB,VRBO,"https://www.houfy.com/329782","https://instagram.com/compassbluelahaina","https://facebook.com/compassbluelahaina"],
 "potentialAction":{"@type":"ReserveAction","target":"https://www.houfy.com/329782"},
}
site = {"@context":"https://schema.org","@type":"WebSite","name":NAME,"url":BASE}

out = head(f"{NAME} | Beachfront studio, 475 Front Street, Lahaina, Maui",
  "Owner-hosted studio in the oceanfront Lahaina Shores building, 475 Front Street, Lahaina, in the Kaanapali area of West Maui. Mountain-view lanai, full kitchen, beach steps from the lobby.",
  "", ld(biz) + "\n" + ld(site))
out += header("home")
out += f'''<main id="main">

<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <p class="where">475 Front Street, Lahaina, in the Kaanapali area of West Maui</p>
      <h1>{NAME}</h1>
      <p class="lede">An owner-hosted studio in the only resort on this stretch of beach. The lanai looks to the West Maui Mountains, the uncrowded sand is an elevator ride away, and it costs far less than the Kaanapali resorts up the coast.</p>
      <div class="hero-actions">
        <a class="btn btn-book" href="{HOUFY}" rel="noopener">Check dates and book</a>
        <a class="btn btn-line" href="#book">Other ways to book</a>
      </div>
      <p class="small">Booking and payment run through Houfy, with no guest service fee. Also on <a href="{AIRBNB}" rel="noopener">Airbnb</a> and <a href="{VRBO}" rel="noopener">VRBO</a>.</p>
      <ul class="facts" aria-label="At a glance">
        <li>Sleeps 3</li><li>Studio, 1 bath</li><li>Full kitchen</li><li>Central A/C</li><li>Pool and hot tub</li><li>Airbnb Guest Favorite</li>
      </ul>
    </div>
    <div class="mosaic">
      {pic("room-orchid","The studio at Compass Blue at Lahaina Shores: queen bed in white linens, ceiling fan, guitar on the wall, and the lanai with mountain views beyond","(min-width: 900px) 34vw, 62vw",True)}
      {pic("room-lanai","The lanai with a hanging nest chair and a table for two, seen from inside the studio","(min-width: 900px) 17vw, 31vw",True)}
      {pic("pool-sunset","Sunset over the ocean from the Lahaina Shores pool deck, palm trees reflected in the pool","(min-width: 900px) 17vw, 31vw",True)}
    </div>
  </div>
</section>

<section class="wrap" aria-labelledby="directions">
  <h2 id="directions" class="skip" style="position:absolute">Mountains one way, ocean the other</h2>
  <div class="compass">
    <div class="mauka">
      {pic("lanai-mountains","The West Maui Mountains under blue sky, seen across the lanai table and nest chair","(min-width: 760px) 45vw, 92vw")}
      <h3>Mountains from your lanai</h3>
      <span class="word">Mauka, toward the mountains</span>
      <p>Your private lanai faces the West Maui Mountains, where rainbows show up most afternoons. Look left for the Lahaina Banyan Tree and a glimpse of the harbor. The hanging nest chair is the seat guests fight over.</p>
    </div>
    <div class="makai">
      {pic("pool-day","The oceanfront pool at Lahaina Shores, with lawn, palm trees and the ocean just beyond","(min-width: 760px) 45vw, 92vw")}
      <h3>Ocean out the lobby</h3>
      <span class="word">Makai, toward the sea</span>
      <p>Lahaina Shores sits on the sand. Ride the elevator down, walk past the pool, and you are on the beach without crossing a road. In whale season, guests watch humpbacks breach from right there.</p>
    </div>
    <div class="rose">{ROSE}</div>
  </div>
</section>

<section class="section" id="studio">
  <div class="wrap">
    <div class="split wide-left">
      <div>
        <h2>The studio</h2>
        <p>Compass Blue is one privately owned studio inside Lahaina Shores Beach Resort, hosted by its owner, Kristie. It is set up for cooking real meals, sleeping well and spending the day outside. It is most comfortable for one or two guests and sleeps three at most.</p>
        <p>The furnishings reflect our family's Lahaina roots, with pieces from The Whaler Ltd., the Front Street shop that was part of old Lahaina.</p>
        <ul class="has">
          <li>Queen bed</li>
          <li>Two Serta armchairs that convert to twin beds</li>
          <li>Full kitchen with dishwasher; guests say nothing is missing</li>
          <li>Private lanai with table and nest chair</li>
          <li>Bathroom with solid doors</li>
          <li>Central air conditioning</li>
          <li>Free WiFi</li>
          <li>Beach towels, chairs and umbrella</li>
          <li>Oceanfront pool and hot tub</li>
          <li>Pau Bakery in the lobby</li>
          <li>24-hour front desk in the building</li>
          <li>Parking: $15 a day, or free on Shaw Street</li>
        </ul>
      </div>
      <div>
        {pic("bathroom","Bathroom at Compass Blue: granite vanity, with the shower and toilet in their own room behind a door","(min-width: 900px) 30rem, 92vw",cls="photo")}
        <h3 style="margin-top:1.25rem">A bathroom with doors</h3>
        <p>Many Lahaina Shores studios were opened up so the toilet and shower share a room with the sink. Ours kept its walls and solid doors. One person can shower while another uses the vanity, which matters when friends or family share a studio.</p>
      </div>
    </div>
    <div class="strip">
      <figure>{pic("bed-lanai","Queen bed facing the lanai and the mountains","(min-width: 760px) 30vw, 82vw")}<figcaption>Wake up facing the mountains</figcaption></figure>
      <figure>{pic("room-lanai","Two armchairs that convert to twin beds, beside the sliding doors to the lanai","(min-width: 760px) 30vw, 82vw")}<figcaption>The two armchairs convert to twin beds</figcaption></figure>
      <figure>{pic("kitchen","Kitchen with wood cabinets, blue tile backsplash, dishwasher, range and microwave","(min-width: 760px) 30vw, 82vw")}<figcaption>Full kitchen with dishwasher</figcaption></figure>
      <figure>{pic("kitchen-stools","Granite breakfast bar with blue velvet stools in front of the kitchen","(min-width: 760px) 30vw, 82vw")}<figcaption>Breakfast bar for two</figcaption></figure>
      <figure>{pic("bath-doorknob","Glass doorknob on the solid bathroom door, with the walk-in shower behind","(min-width: 760px) 30vw, 82vw")}<figcaption>A real door on the bathroom</figcaption></figure>
      <figure>{pic("shower","Tiled walk-in shower with a bench, grab bar and glass doors","(min-width: 760px) 30vw, 82vw")}<figcaption>Walk-in shower with a bench</figcaption></figure>
    </div>
  </div>
</section>

<section class="section tint" id="beach">
  <div class="wrap">
    <h2>What turns up on the beach</h2>
    <p class="lede">Lahaina Shores is the only resort on this stretch of beach, so the sand out front stays uncrowded, nothing like the busy resort strip at Kaanapali. The animals that turn up are wild and on their own schedule, so treat every sighting as luck.</p>
    <div class="three">
      <div>
        <h3>Humpback whales</h3>
        <p>November through May, with the most activity from January through March. Guests watch them breach from the beach. Whale watching boats leave from Lahaina Harbor, 2 to 3 blocks away.</p>
      </div>
      <div>
        <h3>Hawaiian monk seals</h3>
        <p>Endangered, with about 1,600 left according to NOAA. They have hauled out to rest on the beach in front of the building. Stay at least 50 feet back and let them sleep.</p>
      </div>
      <div>
        <h3>Green sea turtles</h3>
        <p>Honu are in the water year-round and sometimes nap on the sand. They are protected. Watch from a distance and let them come and go.</p>
      </div>
    </div>
    <div class="strip">
      <figure>{pic("turtle-beach","Green sea turtle resting on the sand at the water's edge, with palm trees and the Lahaina Shores building behind","(min-width: 760px) 30vw, 82vw")}<figcaption>A honu resting on the beach in front of Lahaina Shores</figcaption></figure>
      <figure>{pic("turtle-snorkel","Underwater photo of a green sea turtle swimming over the reef with a snorkeler at the surface","(min-width: 760px) 30vw, 82vw")}<figcaption>Snorkeling near a honu. Give them room.</figcaption></figure>
      <figure>{pic("hot-tub-night","The hot tub at Lahaina Shores at dusk, under lit palm trees","(min-width: 760px) 30vw, 82vw")}<figcaption>The hot tub after dark</figcaption></figure>
    </div>
    <div class="note"><p>Learn to surf right here: Hi Surf Club and pop-up board rentals are on the beach next door. The water in front stays shallow a long way out, which suits beginner snorkelers.</p></div>
  </div>
</section>

<section class="section" id="location">
  <div class="wrap">
    <h2>Where you are</h2>
    <figure class="wide">{pic("from-the-water","Lahaina Shores seen from the ocean: the building on the beach among palm trees, with the green West Maui Mountains rising behind and a tour boat in the foreground","(min-width: 72rem) 70rem, 92vw")}<figcaption>Lahaina Shores Beach Resort from the water, right on the sand, with the West Maui Mountains behind. Photo: Bill Halsey</figcaption></figure>
    <div class="split">
      <div>
        <p>475 Front Street is the quiet south end of Lahaina's Front Street, in the Kaanapali area of West Maui. It is the same coastline as the Kaanapali resort strip, a few miles south of it: an uncrowded beach and a full kitchen without the big-resort bill, with Whalers Village a short drive away when you want it.</p>
        <ul class="dist">
          <li><span class="d">In the lobby</span><span>Pau Bakery, for coffee and pastries</span></li>
          <li><span class="d">Next door</span><span>Surf lessons and board rentals on the beach</span></li>
          <li><span class="d">2 to 3 blocks</span><span>Lahaina Harbor: whale watching, snorkel trips and sunset sails you can walk to. Check the departure point when you book; some tours leave from Mala or Māʻalaea instead.</span></li>
          <li><span class="d">2 to 3 blocks</span><span>The Lahaina Banyan Tree, planted in 1873</span></li>
          <li><span class="d">Oceanfront walk</span><span>Old Lahaina Luau, Honu Oceanside, Star Noodle, Aloha Mixed Plate, Coco Deck</span></li>
          <li><span class="d">About a mile</span><span><a href="https://www.uluolele.com/" rel="noopener">ʻUlu o Lele Marketplace</a> at Waineʻe and Papalaua Streets, with local shops and the Front Street Fresh food truck</span></li>
          <li><span class="d">1.8 miles</span><span>Foodland Farms and Safeway, or have groceries delivered</span></li>
          <li><span class="d">5 miles</span><span>Whalers Village and the Kaanapali resorts</span></li>
          <li><span class="d">8 to 9 miles</span><span>Kapalua and the Dragon's Teeth trail</span></li>
        </ul>
        <div class="note">
          <p><strong>Shop local.</strong> ʻUlu o Lele Marketplace brings Lahaina's local vendors, shops and food trucks together about a mile from your door. It is a flat stroll, a quick Uber or a short drive.</p>
        </div>
        <p><a href="guide.html">Read the full guest guide</a> for food, parking and airport tips.</p>
      </div>
      <div>
        <svg class="strollmap" viewBox="0 0 640 780" role="img" aria-labelledby="mapTitle mapDesc">
          <title id="mapTitle">Map of Lahaina showing Compass Blue at Lahaina Shores and nearby places</title>
          <desc id="mapDesc">Compass Blue at Lahaina Shores sits on the beach at the south end of Front Street. Lahaina Harbor and the Banyan Tree are 2 to 3 blocks north. ʻUlu o Lele Marketplace is about a mile north. Old Lahaina Luau and nearby restaurants are further up the shore. Kaanapali and Whalers Village are 5 miles north, off the top of the map. The ocean is to the west and the West Maui Mountains to the east.</desc>
          <defs>
            <linearGradient id="sea" x1="0" x2="1" y1="0" y2="0"><stop offset="0" stop-color="#2f7fb8"/><stop offset=".55" stop-color="#56a3cf"/><stop offset="1" stop-color="#9fd3e6"/></linearGradient>
            <linearGradient id="hill" x1="0" x2="1" y1="0" y2="0"><stop offset="0" stop-color="#e3ecdf"/><stop offset=".5" stop-color="#b9d3ad"/><stop offset="1" stop-color="#6f9f72"/></linearGradient>
            <clipPath id="mapclip"><rect width="640" height="780" rx="14"/></clipPath>
          </defs>
          <g clip-path="url(#mapclip)">
            <rect width="640" height="780" fill="#eef2ea"/>
            <!-- mountains (mauka) -->
            <path d="M420 0C450 160 500 330 560 470C590 540 615 640 640 700V0Z" fill="url(#hill)"/>
            <path d="M500 60l40 -34 34 30 30 -22 36 40M520 200l36 -30 30 26 54 -40M560 350l34 -26 46 30" fill="none" stroke="#5c8d62" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" opacity=".55"/>
            <!-- ocean (makai) -->
            <path d="M0 0H152C146 70 150 130 128 190C104 250 96 262 140 318C178 366 206 412 236 462C258 498 262 520 274 548C296 596 322 628 352 668C384 710 410 744 438 780H0Z" fill="url(#sea)"/>
            <!-- surf lines -->
            <path d="M70 120c14 30 6 70 -10 96M96 330c30 34 56 72 78 112M196 560c26 44 58 86 92 126" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-dasharray="2 12" opacity=".8"/>
            <!-- sand in front of the building -->
            <path d="M300 600C322 632 352 668 384 710" fill="none" stroke="#f1dfb4" stroke-width="9" stroke-linecap="round"/>
            <!-- harbor breakwater -->
            <path d="M262 532l-34 14 22 52 34 -12" fill="#7fbfe0" stroke="#5f6f7a" stroke-width="4" stroke-linejoin="round"/>
            <!-- roads -->
            <g fill="none" stroke-linecap="round" stroke-linejoin="round">
              <path d="M250 0C262 120 300 250 352 380C392 478 446 590 540 780" stroke="#fff" stroke-width="11"/>
              <path d="M250 0C262 120 300 250 352 380C392 478 446 590 540 780" stroke="#f3cf73" stroke-width="5"/>
              <path d="M186 0C180 70 184 130 164 190C150 232 152 262 178 302C214 356 242 404 268 452C290 494 300 520 312 546C334 592 362 632 392 672C416 704 446 742 474 780" stroke="#fff" stroke-width="7"/>
              <path d="M186 0C180 70 184 130 164 190C150 232 152 262 178 302C214 356 242 404 268 452C290 494 300 520 312 546C334 592 362 632 392 672C416 704 446 742 474 780" stroke="#c9d2d6" stroke-width="2"/>
              <path d="M392 672L486 648M312 546l98 -40M268 452l104 -44M214 356l112 -48M164 190l110 -20" stroke="#fff" stroke-width="4"/>
            </g>
            <text font-size="14" fill="#5b6770" transform="rotate(60 232 418)" x="232" y="418" text-anchor="middle">Front Street</text>
            <text font-size="13" fill="#8a6d1d" transform="rotate(66 468 606)" x="468" y="606" text-anchor="middle">Hwy 30</text>
            <text font-size="15" fill="#fff" font-style="italic" x="60" y="470">Pacific Ocean</text>
            <text font-size="12" fill="#eaf6fb" x="60" y="488">makai, toward the sea</text>
            <text font-size="15" fill="#2a654d" font-style="italic" x="628" y="420" text-anchor="end">West Maui</text>
            <text font-size="15" fill="#2a654d" font-style="italic" x="628" y="438" text-anchor="end">Mountains</text>
            <text font-size="12" fill="#2a654d" x="628" y="456" text-anchor="end">mauka</text>
            <!-- north arrow to Kaanapali -->
            <g>
              <rect x="268" y="14" width="270" height="52" rx="26" fill="#0f2a43"/>
              <path d="M294 50V30m0 0l-8 9m8 -9l8 9" fill="none" stroke="#ffc83d" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
              <text x="316" y="37" font-size="14" font-weight="700" fill="#fff">Kaanapali and Whalers Village</text>
              <text x="316" y="55" font-size="12.5" fill="#cfe0ee">5 miles north, same coastline</text>
            </g>
            <!-- pins -->
            <g font-size="17" font-weight="700" fill="#0f2a43" paint-order="stroke" stroke="#fff" stroke-width="5" stroke-linejoin="round">
              <a href="https://www.google.com/maps/search/?api=1&amp;query=Old+Lahaina+Luau" rel="noopener"><circle cx="150" cy="176" r="10" fill="#1b5aa6" stroke="#fff" stroke-width="3"/><text x="196" y="150">Old Lahaina Luau</text><text x="196" y="170" font-size="14" font-weight="500" fill="#4c6072">Star Noodle, Honu Oceanside,</text><text x="196" y="188" font-size="14" font-weight="500" fill="#4c6072">Aloha Mixed Plate nearby</text></a>
              <a href="https://www.uluolele.com/" rel="noopener"><circle cx="262" cy="330" r="10" fill="#2a654d" stroke="#fff" stroke-width="3"/><text x="282" y="328">ʻUlu o Lele Marketplace</text><text x="282" y="348" font-size="14" font-weight="500" fill="#4c6072">local vendors and food, about a mile</text></a>
              <a href="https://www.google.com/maps/search/?api=1&amp;query=Lahaina+Banyan+Court+Park" rel="noopener"><circle cx="318" cy="520" r="10" fill="#2a654d" stroke="#fff" stroke-width="3"/><text x="338" y="518">Banyan Tree</text><text x="338" y="538" font-size="14" font-weight="500" fill="#4c6072">2 to 3 blocks</text></a>
              <a href="https://www.google.com/maps/search/?api=1&amp;query=Lahaina+Harbor" rel="noopener"><circle cx="268" cy="556" r="10" fill="#1b5aa6" stroke="#fff" stroke-width="3"/><text x="66" y="560">Lahaina Harbor</text><text x="66" y="580" font-size="14" font-weight="500" fill="#0f2a43">boat tours you walk to</text></a>
              <a href="https://www.google.com/maps/search/?api=1&amp;query=475+Front+Street+Lahaina+HI" rel="noopener"><circle cx="362" cy="668" r="22" fill="#ffc83d" opacity=".35" stroke="none"/><circle cx="362" cy="668" r="13" fill="#ffc83d" stroke="#0f2a43" stroke-width="3"/><text x="118" y="688" font-size="18">Compass Blue</text><text x="118" y="709" font-size="18">at Lahaina Shores</text><text x="118" y="729" font-size="14" font-weight="500" fill="#0f2a43">beach, pool, bakery, surf lessons</text></a>
            </g>
            <text x="626" y="768" font-size="11" fill="#4c6072" text-anchor="end">Simplified map, not to scale. Tap a pin for directions.</text>
          </g>
        </svg>
        <figure style="margin:1.5rem 0 0">{pic("lobby-ocean","The Lahaina Shores lobby, with seating and glass doors opening onto the pool and the ocean","(min-width: 900px) 40vw, 92vw",cls="photo")}<figcaption class="small" style="margin-top:.45rem">The lobby opens onto the pool and the ocean</figcaption></figure>
      </div>
    </div>
  </div>
</section>

<section class="section tint" id="reviews">
  <div class="wrap">
    <h2>What guests say</h2>
    <p class="lede">Kristie is an Airbnb Superhost with 13 years of hosting, and this studio is an Airbnb Guest Favorite. These are recent Airbnb reviews, quoted as written.</p>
    <div class="quotes">
      <blockquote><p>“Kristie was an outstanding host and this place exceeded our expectations. The setting is stunning, with its own oceanfront pool area, and the building is well maintained with friendly staff on site. The bed was extremely comfortable, and the standout was the outdoor space overlooking the West Maui mountains.”</p><cite>Carlos, September 2026</cite></blockquote>
      <blockquote><p>“Kristie's place is in a great location, right in front of the ocean. The apartment is equipped with everything; nothing is missing, even for going to the beach and leisure activities. Kristie was very kind, responsive and helpful.”</p><cite>Beatrice, October 2026</cite></blockquote>
      <blockquote><p>“Love Kristie's place. Specially having the beach and the pool steps away. Kristie was very communicative with my wife's concerns about the weather and she provided info on things to do. We will definitely return.”</p><cite>Edna, September 2026</cite></blockquote>
      <blockquote><p>“Kristie is such an amazing host! She went above and beyond to make our stay a wonderful one! The condo was so clean and we felt right at home. We really loved staying at her place for our anniversary.”</p><cite>Jeffrey, September 2026</cite></blockquote>
      <blockquote><p>“We loved our stay! The location was perfect. It was quiet and peaceful and not overcrowded at all. We will definitely return!”</p><cite>Shirley, November 2026</cite></blockquote>
      <div>
        <h3>Read every review where it was posted</h3>
        <p>Current ratings and all reviews are on the listing pages: <a href="{AIRBNB}" rel="noopener">Airbnb</a>, <a href="{VRBO}" rel="noopener">VRBO</a> and <a href="{HOUFY}" rel="noopener">Houfy</a>.</p>
      </div>
    </div>
  </div>
</section>

<section class="section book" id="book">
  <div class="wrap book-grid on-dark">
    <div>
      <h2>Book your stay</h2>
      <p>Booking direct on Houfy avoids the platform fees built into Airbnb and VRBO prices. Houfy shows the live calendar and takes payment.</p>
      <p><a class="btn btn-book" href="{HOUFY}" rel="noopener">Check dates and book on Houfy</a></p>
    </div>
    <div>
      <p>Prefer a platform you already use? Book and message there. It is the same studio and the same host.</p>
      <ul class="ways">
        <li><a href="{AIRBNB}" rel="noopener">Book on Airbnb</a><span>Message Kristie through Airbnb</span></li>
        <li><a href="{VRBO}" rel="noopener">Book on VRBO</a><span>Message Kristie through VRBO</span></li>
      </ul>
    </div>
  </div>
</section>

<section class="section map" aria-labelledby="find">
  <div class="wrap">
    <h2 id="find">Find us</h2>
    <p>Lahaina Shores Beach Resort, 475 Front Street, Lahaina, HI 96761. <a href="https://www.google.com/maps/search/?api=1&amp;query=475+Front+Street+Lahaina+HI+96761" rel="noopener">Open in Google Maps</a></p>
    <iframe src="https://maps.google.com/maps?q=20.8672205,-156.6751196&amp;z=16&amp;output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Map showing 475 Front Street, Lahaina, HI"></iframe>
  </div>
</section>

</main>
''' + FOOT
open(sys.argv[1] + "/index.html", "w").write(out)
