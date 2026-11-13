import sys
from common import *
ldj = ld({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":NAME,"item":BASE},{"@type":"ListItem","position":2,"name":"Guest guide","item":BASE+"guide.html"}]})
out = head(f"Guest guide | {NAME}, Maui", "The owner's guide to staying at Compass Blue at Lahaina Shores, 475 Front Street, Lahaina: airport drive, parking, food, groceries, whale watching, surf lessons and what is open in Lahaina.", "guide.html", ldj)
out += header("guide")
secs=[("getting-here","Getting here"),("the-studio","In the studio"),("beach","Beach and wildlife"),("on-the-water","On the water"),("food","Food and coffee"),("local","Shop local"),("groceries","Groceries"),("packing","What to pack"),("parking","Parking and getting around"),("walks","Short walks"),("further","Further afield"),("groups","Groups")]
out += '<main id="main">\n<div class="page-head"><div class="wrap">\n<h1>Guest guide</h1>\n<p class="lede">What Kristie tells every guest of Compass Blue at Lahaina Shores, 475 Front Street, Lahaina, in the Kaanapali area of West Maui.</p>\n<ul class="toc">\n'
out += "".join(f'<li><a href="#{i}">{t}</a></li>\n' for i,t in secs) + '</ul>\n</div></div>\n<div class="prose">\n'
out += f'''
<h2 id="getting-here">Getting here from Kahului Airport (OGG)</h2>
<p>Plan on 45 to 55 minutes from Kahului Airport to Lahaina Shores Beach Resort, 475 Front Street, Lahaina, HI 96761, on Highway 30 (Honoapiilani Highway). Allow more time in afternoon traffic or if you stop for groceries on the way.</p>
<p>Most guests rent a car at the airport, which also makes Haleakalā, the Road to Hana and upcountry Maui easy. Uber and Lyft work from the airport too if you would rather not drive after a long flight.</p>

<h2 id="the-studio">In the studio</h2>
<ul>
<li><strong>Beds:</strong> a queen bed, plus two Serta armchairs that each unfold into a twin bed. The gray quilted covers in the drawers go on as mattress pads, and protect the chairs by day. Most comfortable for 1 or 2; sleeps 3.</li>
<li><strong>Kitchen:</strong> range and oven, full-size refrigerator, microwave, dishwasher and toaster, with a breakfast bar for two. The coffee machine takes Nespresso pods and K-cups; there are usually some here, but bring your favorites.</li>
<li><strong>Lanai:</strong> faces the West Maui Mountains, with a table for two and a hanging nest chair. Rainbows are frequent, mostly in the afternoon. Look left for the Banyan Tree and a glimpse of the harbor.</li>
<li><strong>Bathroom:</strong> solid doors and a walk-in shower. There are also restroom stalls by the pool, handy on beach days.</li>
<li><strong>Beach gear:</strong> beach towels, chairs and an umbrella are in the unit. Rinse off at the de-sand showers and change at the pool stalls.</li>
</ul>
<div class="note"><p><strong>Yes, the snacks on the counter are for you.</strong> For a very short stay, ask ahead and Kristie will leave milk, coffee or other basics.</p></div>

<h2 id="beach">Beach and wildlife</h2>
<p>Lahaina Shores is an oceanfront building, and the only resort on this stretch of beach. From the lobby you walk past the pool and onto uncrowded sand.</p>
<h3>Humpback whales, November through May</h3>
<p>Maui's waters are winter breeding and calving grounds for North Pacific humpbacks. In season it is common to see breaches, tail slaps and blows from the beach in front of the building, most often from January through March.</p>
<h3>Hawaiian monk seals</h3>
<p>Monk seals are endangered; NOAA estimates about 1,600 remain. They have rested on the beach in front of the building. If you see one, stay at least 50 feet away. Disturbing them is against federal law.</p>
<h3>Green sea turtles</h3>
<p>Honu visit year-round. They are protected too. A turtle napping on the sand is doing fine; leave it be.</p>

<h2 id="on-the-water">On the water</h2>
<p><strong>Lahaina Harbor is 2 to 3 blocks away on foot.</strong> Whale watching, snorkel and dive trips, fishing charters and sunset sails leave from there. Kristie recommends Hawaii Ocean Project for whale watching.</p>
<div class="note"><p><strong>Check where your boat leaves from.</strong> Each operator keeps its own schedule, and it changes by day. Lahaina Harbor, Mala Wharf and Māʻalaea Harbor are three different places, and all of them can come up in one search. You walk to the Lahaina one; the others are a drive.</p></div>
<p><strong>Surf lessons are next door.</strong> Hi Surf Club teaches on the beach beside Lahaina Shores, and pop-up board rentals set up there too.</p>
<p>Catamarans also load straight off Kaanapali Beach in front of Whalers Village, about 5 miles north. After a sunset sail, most guests take an Uber back.</p>
<div class="note"><p><strong>Snorkeling:</strong> the water in front stays shallow a long way out, which is good for beginners. Use a well-fitted mask and fins. Skip full-face masks.</p></div>

<h2 id="food">Food and coffee</h2>
<h3>Pau Bakery, in the Lahaina Shores lobby</h3>
<p>Coffee and pastries without leaving the building. <a href="https://www.houfy.com/kristiehalsey/posts/pau-bakery-makes-an-entrance-at-lahaina-shores-beach-resort-14516170" rel="noopener">Read the story</a>.</p>
<h3>The Coffee Stop</h3>
<p>A local walk-up, food truck style, at Lahainaluna Road and the main road. Go before 10am to beat the heat. It is a flat mile on the lower road, which is less highway-like. Starbucks is 1.8 miles away.</p>
<h3>Along the oceanfront walk</h3>
<p>Old Lahaina Luau, Honu Oceanside, Star Noodle, Aloha Mixed Plate and Coco Deck are the closest places to eat. Book the luau well ahead; it sells out weeks in advance in busy months.</p>
<h3>Front Street Fresh</h3>
<p>Now a food truck at ʻUlu o Lele Marketplace, about a mile away. Breakfast burritos, smoothies, burgers and french toast. Check their Instagram for hours and specials.</p>
<h3>Cool Cat Cafe, Whalers Village</h3>
<p>Burgers in Kaanapali, about 5 miles north. They validate parking (see below).</p>
<h3>Canoe Club, by the Westin Villas</h3>
<p>A sports bar on the water along the Kaanapali boardwalk. Good for a drink at sunset.</p>

<h2 id="local">Shop local at ʻUlu o Lele Marketplace</h2>
<p><a href="https://www.uluolele.com/" rel="noopener">ʻUlu o Lele Marketplace</a> is at Waineʻe and Papalaua Streets, about a mile from Compass Blue. Walk it or make it a short drive. Local retailers and restaurants share the space, and what you spend goes to the small businesses that kept Lahaina going.</p>
<p>Many long-time Front Street shops have reopened at the Cannery and Keawe Hub area, a couple of blocks from ʻUlu o Lele. <a href="https://www.houfy.com/kristiehalsey/posts/long-time-lahaina-front-street-shops-are-still-here-14515818" rel="noopener">Here is where to find them</a>.</p>

<h2 id="groceries">Groceries</h2>
<p>Foodland Farms and Safeway are 1.8 miles away. Many guests have groceries delivered by Safeway, Demming Delivers, or Walmart+ if they have it, so the kitchen is stocked the first night. If you can, bring your first few meals and easy breakfast items. The real time saver is getting outside right away.</p>

<h2 id="packing">What to pack</h2>
<ul>
<li><strong>Skip checked luggage.</strong> Pack swimsuits, sarongs and laundry pods. Laundry is $5.50 a load, so re-wearing costs less than baggage fees.</li>
<li><strong>Leave at home:</strong> nightclub wear and dress shoes.</li>
<li><strong>Towels:</strong> quick-dry beach towels and bath towels are provided. Heavy beach users may want extras.</li>
<li><strong>Sun:</strong> hydrate, wear a hat, and use regular lotion sunscreen. Spray leaves a sticky residue and harms the reef.</li>
<li><strong>Coffee:</strong> the machine takes Nespresso pods and K-cups. Bring your favorites.</li>
</ul>

<h2 id="parking">Parking and getting around</h2>
<h3>At Lahaina Shores</h3>
<p>The resort lot is $15 per day. Street parking on Shaw Street is free; read the posted signs before you walk away.</p>
<h3>At Whalers Village</h3>
<p>The garage charges, and a lost ticket can cost $50. Eat at Cool Cat Cafe and ask for validation, or take an Uber and skip parking altogether.</p>
<h3>Around the island</h3>
<p>You can do the beach, harbor, Banyan Tree and bakery on foot. A rental car is worth it for Haleakalā, the Road to Hana and upcountry.</p>

<h2 id="walks">Short walks</h2>
<ul>
<li><strong>Lahaina Banyan Tree, 2 to 3 blocks.</strong> Planted in 1873 and the green heart of town.</li>
<li><strong>Lahaina Harbor, 2 to 3 blocks.</strong> Boats, and the old seafaring heart of town.</li>
<li><strong>The oceanfront sidewalk.</strong> Open ocean, waves, rocks and wildlife. Not much else, and that is the point.</li>
</ul>
<div class="note"><p><strong>A note on Front Street.</strong> Parts of historic Front Street are being rebuilt. If you walk past, please be respectful of the people who live and work here.</p></div>

<h2 id="further">Further afield</h2>
<ul>
<li><strong>Whalers Village and Kaanapali Beach, 5 miles.</strong> Shops and restaurants on the beach, including Leilani's and Hula Grill.</li>
<li><strong>Honokowai, 5.5 miles.</strong> Food trucks by Times Market.</li>
<li><strong>Kapalua and Dragon's Teeth, 8 to 9 miles.</strong> Coastal trail, views and the walking labyrinth.</li>
</ul>
<div class="note"><p><strong>Resort cats:</strong> the cats you see around the Kaanapali resorts are fed and looked after by staff. Most are friendly. Wash your hands afterward.</p></div>

<h2 id="groups">Groups and special occasions</h2>
<p>Compass Blue sleeps 3. Families and wedding groups often book several units in Lahaina Shores, so each household has its own kitchen, and meet on the beach at sunset. Message Kristie through Houfy, Airbnb or VRBO to coordinate.</p>

<p style="margin-top:3rem"><a class="btn btn-book" href="{HOUFY}" rel="noopener">Check dates and book</a> &nbsp; <a href="faq.html">Questions and answers</a></p>
</div>
</main>
''' + FOOT
open(sys.argv[1] + "/guide.html", "w").write(out)
