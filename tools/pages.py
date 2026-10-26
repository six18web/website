"""Content for the service pages. Edit text here, then run: python3 tools/build.py
Keep prices and package contents in step with the Pricing section of index.html."""

STEPS = """
  <section class="process">
    <div class="wrap">
      <p class="eyebrow">How it works</p>
      <h2 style="margin-top:.75rem">From first call to live site in about two weeks.</h2>
      <div class="steps">
        <div class="step"><h3>Free review</h3><p>We look at how you show up on Google and on a phone, and walk you through what's working and what isn't.</p><span class="when">10 minutes</span></div>
        <div class="step"><h3>Written quote</h3><p>A flat price and a plain list of what you get. Nothing starts until you say yes.</p><span class="when">Within 2 days</span></div>
        <div class="step"><h3>Build</h3><p>You send photos and a few details. We write the copy, build the site, and send you a preview to approve.</p><span class="when">About 2 weeks</span></div>
        <div class="step"><h3>Launch</h3><p>We connect your domain, set up Google, test every button on real phones, and show you how to make small changes.</p><span class="when">Same week</span></div>
      </div>
    </div>
  </section>
"""

WEB_DESIGN = dict(
    path="/web-design/",
    crumb="Web design",
    service_name="Small business web design",
    price="950",
    title="Small Business Web Design in Edwardsville, IL | Six18 Web",
    desc="Phone-first websites for small businesses in Edwardsville, Glen Carbon & the Metro East. Flat prices from $950, live in about two weeks. You own it.",
    eyebrow="Web design · Edwardsville &amp; Glen Carbon",
    h1="Small business web design that <em>gets you calls.</em>",
    lede="We design and build websites for local service businesses, shops, and restaurants: fast on a phone, easy to call from, and set up so the people searching nearby can actually find you.",
    price_line="Starter Site <b>$950</b> · Business Site <b>$2,800</b> · Flat price, written quote first",
    faq_h2="Web design questions.",
    cta_h2="Not sure which site you need?",
    body="""
  <section>
    <div class="wrap">
      <div class="problems-head">
        <p class="eyebrow">What every site includes</p>
        <h2>Built for the way your customers actually search.</h2>
        <p class="lede">Most people find a local business on their phone, in a hurry, often standing in a parking lot. Every Six18 site is designed for that moment first.</p>
      </div>
      <ul class="feature-grid">
        <li><h3>Phone-first design</h3><p>Designed on a phone screen, then scaled up. No pinching, no zooming, no tiny links.</p></li>
        <li><h3>Tap-to-call up top</h3><p>Your phone number and a quote button are the first things people see, on every page.</p></li>
        <li><h3>Secure from day one</h3><p>The padlock in the address bar, so no browser ever shows your customers a "Not secure" warning.</p></li>
        <li><h3>Written for Google, too</h3><p>Page titles, headings, and descriptions that name your trade and your towns, the way people search.</p></li>
        <li><h3>Google Business Profile</h3><p>We set up or clean up your Google listing so it matches your site and points to the right number.</p></li>
        <li><h3>Yours to keep</h3><p>Your domain, your content, every login. If you ever leave, the site goes with you.</p></li>
      </ul>
    </div>
  </section>

  <section class="checkup">
    <div class="wrap block">
      <p class="eyebrow">Two ways to start</p>
      <h2 style="margin-top:.75rem">Pick the site that fits where you are.</h2>
      <div class="pricing-grid two-up">
        <article class="plan">
          <h3>Starter Site</h3>
          <p class="price">$950<small> one time</small></p>
          <p class="for">For owners with no website yet, or just a Facebook page.</p>
          <ul><li>One scrolling page, phone-first</li><li>Services, photos, hours, and map</li><li>Tap-to-call and contact form</li><li>Google Business Profile setup</li></ul>
        </article>
        <article class="plan feature">
          <span class="badge">Most popular</span>
          <h3>Business Site</h3>
          <p class="price">$2,800<small> one time</small></p>
          <p class="for">For contractors and shops that want steady leads from search.</p>
          <ul><li>Up to 6 pages, one per service</li><li>Quote or booking form</li><li>Town pages for your service area</li><li>Reviews and before/after gallery</li><li>Built to accessibility standards (WCAG 2.1 AA)</li><li>Local SEO setup</li></ul>
        </article>
      </div>
      <p class="price-note">Domain registration is billed at cost. Hosting and updates are optional through the $89/month Care Plan, or we hand you the keys. Larger projects get a written quote after the free review.</p>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div class="prose">
        <p class="eyebrow">Who we build for</p>
        <h2 style="margin-top:.75rem">Busy owners who'd rather be on the job.</h2>
        <p>Roofers, plumbers, HVAC and electrical contractors, landscapers, salons and barbers, auto shops, restaurants, and the small shops on Main Street. Businesses with great reviews and a website that hasn't kept up.</p>
        <p>You don't need to write anything or learn any software. Send us phone photos of real jobs and answer a few questions. We write the copy, build the site, and walk you through a preview before anything goes live.</p>
      </div>
      <div class="prose">
        <p class="eyebrow">Local, and remote</p>
        <h2 style="margin-top:.75rem">Right here in the 618.</h2>
        <p>We're based in Edwardsville and Glen Carbon and happy to meet at your shop, your job site, or over coffee anywhere in Madison County and the Metro East. Outside the area, everything works just as well over a short video call.</p>
        <div class="area"><span class="home">Edwardsville</span><span class="home">Glen Carbon</span><span>Maryville</span><span>Collinsville</span><span>Troy</span><span>Granite City</span><span>Alton</span><span>Highland</span></div>
      </div>
    </div>
  </section>
""" + STEPS,
    faqs=[
        ("How much does a small business website cost?", "A Starter Site is $950 and a Business Site is $2,800, both flat prices. You get a written quote before any work starts, and there are no surprise invoices."),
        ("How long does it take?", "About two weeks from the day we get your photos and details. Most of the waiting is usually on photos, so we tell you exactly what to shoot."),
        ("Do I have to write the content?", "No. We write the copy from a short conversation with you, and you approve every word before launch."),
        ("Will my new website show up on Google?", "We build every site so Google can read your trade and your towns, and we set up your Google Business Profile. New sites usually take a few weeks to be indexed and a few months to climb in local results. Nobody can honestly guarantee a #1 spot, and we won't."),
        ("Can I make changes myself?", "Yes. We show you how to update hours, prices, and photos. If you'd rather text us the changes, the Care Plan includes up to an hour of edits a month."),
        ("What if I already have a website?", "It may only need fixing, not replacing. The free review tells you which. See <a href=\"/website-repair/\">website fixes</a>."),
    ],
)

WEBSITE_REPAIR = dict(
    path="/website-repair/",
    crumb="Website fixes",
    service_name="Website repair and fixes",
    price="199",
    title="Website Repair & Fixes for Small Businesses | Six18 Web",
    desc="Fix a \"Not secure\" warning, broken forms, phone links that don't dial, and old pages. Website fixes from $199 on WordPress, Wix, Squarespace & more.",
    eyebrow="Website fixes · from $199",
    h1="Website repair, <em>without starting over.</em>",
    lede="Your website is mostly fine, but something is costing you calls: a security warning, a phone number that won't dial, a form that goes nowhere. We find it, fix it, and leave the rest alone.",
    price_line="Site Fix-It <b>from $199</b> · Written quote first · Works on most platforms",
    faq_h2="Website repair questions.",
    cta_h2="Not sure what's broken?",
    body="""
  <section>
    <div class="wrap">
      <div class="problems-head">
        <p class="eyebrow">What we fix most</p>
        <h2>Small problems that quietly cost you customers.</h2>
        <p class="lede">These are the issues we see over and over on local business websites. Most take an hour or two to fix, and customers notice every one of them.</p>
      </div>
      <ul class="feature-grid">
        <li><h3>"Not secure" warnings</h3><p>Missing or expired security certificates (SSL), so the padlock shows and browsers stop scaring people away.</p></li>
        <li><h3>Phone numbers that don't dial</h3><p>Tap-to-call links that work, and the right number everywhere, including old numbers buried on inner pages.</p></li>
        <li><h3>Broken contact forms</h3><p>Forms that silently fail or send to an inbox nobody checks. We test them end to end.</p></li>
        <li><h3>Broken links and old pages</h3><p>Dead links, discontinued services, last year's specials, and the "© 2019" footer.</p></li>
        <li><h3>Hard to use on a phone</h3><p>Text too small, buttons too close together, pages that need pinching and zooming.</p></li>
        <li><h3>A messy Google listing</h3><p>Page titles that don't name your trade or town, and a Google Business Profile that disagrees with your site.</p></li>
      </ul>
    </div>
  </section>

  <section class="checkup">
    <div class="wrap two">
      <div class="prose">
        <p class="eyebrow">How it works</p>
        <h2 style="margin-top:.75rem">We fix it where it lives.</h2>
        <p>You don't need to move your website or change hosts. For the length of the job, you add us as a user on your site (WordPress, Wix, Squarespace, GoDaddy, Shopify, and most others allow this), or share access another way you're comfortable with.</p>
        <p>We make the fixes, test everything on real phones, and send you a short list of what changed. When we're done, you remove our access. Nothing is changed that you didn't approve.</p>
      </div>
      <div>
        <article class="plan feature">
          <span class="badge">Most common</span>
          <h3>Site Fix-It</h3>
          <p class="price">$199<small> starting</small></p>
          <p class="for">Your site is mostly fine but something's broken.</p>
          <ul><li>Security certificate (padlock)</li><li>Click-to-call and wrong-number fixes</li><li>Broken links, forms, and old pages</li><li>Google title and listing cleanup</li></ul>
        </article>
        <p class="price-note">Bigger problems get a written quote after the free review. If a rebuild would cost you less than patching, we'll say so, and the <a href="/web-design/">Starter Site</a> starts at $950.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div class="prose">
        <p class="eyebrow">Fix or rebuild?</p>
        <h2 style="margin-top:.75rem">Straight advice, either way.</h2>
        <p>If your site is on a platform that still gets updates, looks decent on a phone, and you can log in to it, it's usually worth fixing. If it's built on something abandoned, nobody has the login, or every page needs work, a rebuild is often cheaper in the long run.</p>
        <p>The free 10-minute review tells you which, in plain English, before you spend anything.</p>
      </div>
      <div class="prose">
        <p class="eyebrow">Keep it fixed</p>
        <h2 style="margin-top:.75rem">Stop it from breaking again.</h2>
        <p>Most of these problems come back because nobody is watching the site. The <a href="/#pricing">Care Plan</a> ($89/month, no contract) covers hosting, the security certificate, updates, daily backups, and up to an hour of edits a month.</p>
      </div>
    </div>
  </section>
""",
    faqs=[
        ("How much does it cost to fix a website?", "Most small fixes fall under the Site Fix-It plan, which starts at $199. Bigger jobs get a flat written quote after the free review, so you know the price before we start."),
        ("Do I have to move my website to you?", "No. We work on your site where it's hosted now. You add us as a user or share access for the job, and remove it when we're done."),
        ("Which platforms do you work on?", "WordPress, Wix, Squarespace, GoDaddy Website Builder, Shopify, and most hand-built sites. If we can't help with yours, we'll tell you up front."),
        ("How fast can you fix it?", "Small fixes are usually done within a few business days of getting access. A security warning or broken phone link usually goes first."),
        ("What if my old web person won't respond?", "That's common. As long as you can get into your domain account (where you bought your web address), we can usually recover access or move you somewhere you control."),
    ],
)

LOCAL_SEO = dict(
    path="/local-seo/",
    crumb="Local SEO",
    service_name="Local SEO and Google Business Profile management",
    price="399",
    title="Local SEO & Google Business Profile Help | Six18 Web",
    desc="Show up in Google Maps and local search when nearby customers look for what you do. Google Business Profile, reviews, and listings for $399/month.",
    eyebrow="Local SEO · Google Maps &amp; local search",
    h1="Show up when <em>someone nearby searches.</em>",
    lede="When someone searches \"roofer near me\" or \"best salon in Edwardsville,\" Google shows a map with three businesses. Local SEO is the steady work of earning one of those spots, and keeping it.",
    price_line="Local Search <b>$399/month</b> · Month to month · One-page report every month",
    faq_h2="Local SEO questions.",
    cta_h2="See where you show up today.",
    body="""
  <section>
    <div class="wrap">
      <div class="problems-head">
        <p class="eyebrow">What moves the needle</p>
        <h2>The map is won with a few things, done every month.</h2>
        <p class="lede">Google ranks local businesses on how relevant they look, how close they are to the person searching, and how trusted they seem. You can't move your shop, but you can work on the rest.</p>
      </div>
      <ul class="feature-grid">
        <li><h3>Google Business Profile</h3><p>Complete, accurate, and active: the right categories and services, fresh photos, and regular posts.</p></li>
        <li><h3>Reviews</h3><p>A simple way to ask happy customers for a Google review after the job, and replies to every review you get.</p></li>
        <li><h3>Matching listings</h3><p>Your name, number, and address the same on Bing, Apple Maps, Yelp, Facebook, and local directories.</p></li>
        <li><h3>A website Google can read</h3><p>Pages that clearly say what you do and which towns you serve, linked from your Google listing.</p></li>
      </ul>
    </div>
  </section>

  <section class="checkup">
    <div class="wrap two">
      <div class="prose">
        <p class="eyebrow">Monthly plan</p>
        <h2 style="margin-top:.75rem">We do the work. You get the calls.</h2>
        <p>Local SEO isn't a one-time switch. Your competitors post, collect reviews, and update their listings every month, so the plan does the same for you, and reports back in plain English.</p>
        <p>Already have a site from somewhere else? That's fine. Local Search works with the website you have.</p>
      </div>
      <div>
        <article class="plan feature">
          <span class="badge">More calls</span>
          <h3>Local Search</h3>
          <p class="price">$399<small> / month</small></p>
          <p class="for">Show up higher when people nearby search for what you do.</p>
          <ul><li>Everything in the Care Plan</li><li>Google Business Profile posts and photos</li><li>Review requests sent to your customers</li><li>Directory listings fixed to match</li><li>A one-page report each month: calls, clicks, rankings</li></ul>
        </article>
        <p class="price-note">Month to month; cancel any time and keep everything. Every <a href="/web-design/">Business Site</a> also includes a one-time local SEO setup.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div class="prose">
        <p class="eyebrow">Honest expectations</p>
        <h2 style="margin-top:.75rem">No guarantees. Real progress.</h2>
        <p>Anyone promising you the #1 spot on Google is guessing. What we promise is the work: done every month, tracked, and reported, so you can see calls and clicks move.</p>
        <p>The monthly report shows views, calls, and rankings side by side, so you can see what's moving and decide for yourself whether it's worth it.</p>
      </div>
      <div class="prose">
        <p class="eyebrow">Where we work</p>
        <h2 style="margin-top:.75rem">Metro East and beyond.</h2>
        <p>We know the local search landscape here: Edwardsville, Glen Carbon, Maryville, Collinsville, Troy, and the rest of Madison County. Local SEO works the same way for service businesses anywhere in the U.S., so we work with owners nationwide too.</p>
        <div class="area"><span class="home">Edwardsville</span><span class="home">Glen Carbon</span><span>Maryville</span><span>Collinsville</span><span>Troy</span><span>Granite City</span><span>Alton</span><span>Highland</span></div>
      </div>
    </div>
  </section>
""",
    faqs=[
        ("What is local SEO?", "It's the work that helps your business show up in Google Maps and the local results when someone nearby searches for what you do: your Google Business Profile, reviews, matching listings, and a website that clearly names your services and towns."),
        ("How long does local SEO take to work?", "It's a months-long effort, not a switch. Early changes usually show up first as more views of your Google listing; bigger ranking gains build over several months as reviews add up. The monthly report shows you what's moving."),
        ("Do I need a website for local SEO?", "It helps a lot, since Google uses your site to understand what you do. But we can start with your Google Business Profile and listings, and add a site later."),
        ("Am I locked into a contract?", "No. Local Search is month to month. Cancel any time and you keep your Google profile, listings, reviews, and website."),
        ("What's the difference between the Care Plan and Local Search?", "The Care Plan ($89/month) keeps your website running: hosting, security, backups, and small edits. Local Search ($399/month) includes all of that, plus the monthly work to bring in more calls from Google."),
    ],
)

PAGES = [WEB_DESIGN, WEBSITE_REPAIR, LOCAL_SEO]
