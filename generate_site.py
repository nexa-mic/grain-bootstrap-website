"""Generate the deployable static GRAIN holding website.

Run from the brain-bootstrap-website directory with: python3 generate_site.py
The generated HTML lives in site/. Assets and CSS are maintained directly there.
"""

from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parent / "site"
EMAIL = "info@grainglobal.org"
PHONE_DISPLAY = "(+233) 123-456-7890"
PHONE_LINK = "+2331234567890"


def nav(active: str) -> str:
    items = [
        ("Home", "./", "home"),
        ("Our Organization", "our-organization.html", "organization"),
        ("Events", "events.html", "events"),
        ("News & Updates", "news.html", "news"),
        ("Contact Us", "contact.html", "contact"),
    ]
    links = ""
    for label, url, key in items:
        active_class = " active" if active == key else ""
        current_attr = ' aria-current="page"' if active == key else ""
        links += f'<li class="nav-item"><a class="nav-link{active_class}" href="{url}"{current_attr}>{label}</a></li>'
    return f"""
    <div class="top-strip py-2">
      <div class="container d-flex justify-content-between align-items-center gap-3">
        <span>Global research <span class="mx-2 text-warning">•</span> Advisory <span class="mx-2 text-warning">•</span> Innovation</span>
        <div class="d-flex gap-4"><a href="mailto:{EMAIL}"><i class="bi bi-envelope me-2" aria-hidden="true"></i>{EMAIL}</a><a href="tel:{PHONE_LINK}"><i class="bi bi-telephone me-2" aria-hidden="true"></i>{PHONE_DISPLAY}</a></div>
      </div>
    </div>
    <header class="site-header sticky-top">
      <nav class="navbar navbar-expand-lg" aria-label="Main navigation">
        <div class="container">
          <a class="navbar-brand py-0" href="./" aria-label="GRAIN home"><img class="brand-logo" src="assets/images/grain-logo-dark.svg?v=3" alt="GRAIN"></a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#mainNavigation" aria-controls="mainNavigation" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
          <div class="collapse navbar-collapse" id="mainNavigation">
            <ul class="navbar-nav ms-auto me-lg-3">{links}</ul>
            <a class="btn btn-grain nav-cta" href="contact.html">Start a conversation <i class="bi bi-arrow-up-right" aria-hidden="true"></i></a>
          </div>
        </div>
      </nav>
    </header>"""


def footer() -> str:
    return f"""
    <footer class="site-footer">
      <div class="container">
        <div class="row g-5">
          <div class="col-lg-5">
            <a href="./" aria-label="GRAIN home"><img class="footer-logo" src="assets/images/grain-logo-light.svg?v=3" alt="GRAIN"></a>
            <p class="mt-3 mb-0" style="max-width: 390px">Connecting African scholarship with the research, advisory and innovation pathways needed to turn ideas into practical solutions.</p>
          </div>
          <div class="col-sm-6 col-lg-3">
            <h3>Explore</h3>
            <ul><li><a href="our-organization.html">Our Organization</a></li><li><a href="events.html">Events</a></li><li><a href="news.html">News & Updates</a></li><li><a href="contact.html">Contact Us</a></li></ul>
          </div>
          <div class="col-sm-6 col-lg-4">
            <h3>Get in touch</h3>
            <ul><li><a href="mailto:{EMAIL}"><i class="bi bi-envelope me-2" aria-hidden="true"></i>{EMAIL}</a></li><li><a href="tel:{PHONE_LINK}"><i class="bi bi-telephone me-2" aria-hidden="true"></i>{PHONE_DISPLAY}</a></li></ul>
            <p class="mt-3 mb-0">From scholarship to enterprise.</p>
          </div>
        </div>
        <div class="footer-bottom d-flex flex-wrap justify-content-between gap-2">
          <span>© <span data-year>2026</span> GRAIN. All rights reserved.</span>
          <a class="back-top" href="#top">Back to top <i class="bi bi-arrow-up" aria-hidden="true"></i></a>
        </div>
      </div>
    </footer>"""


def layout(name: str, title: str, description: str, active: str, body: str) -> None:
    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#005252">
  <meta name="description" content="{escape(description, quote=True)}">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{escape(title, quote=True)}">
  <meta property="og:description" content="{escape(description, quote=True)}">
  <title>{escape(title)}</title>
  <link rel="icon" type="image/svg+xml" href="assets/images/grain-logo-dark.svg?v=3">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.13.1/font/bootstrap-icons.min.css" rel="stylesheet">
  <link href="assets/css/styles.css?v=5" rel="stylesheet">
</head>
<body id="top">
  <a class="skip-link" href="#main">Skip to main content</a>
  {nav(active)}
  <main id="main">{body}</main>
  {footer()}
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js" integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI" crossorigin="anonymous"></script>
  <script src="assets/js/site.js" defer></script>
</body>
</html>
"""
    (ROOT / name).write_text(html, encoding="utf-8")


def inner_hero(title: str, intro: str, current: str) -> str:
    return f"""
    <section class="inner-hero">
      <div class="container">
        <nav aria-label="Breadcrumb"><ol class="breadcrumb"><li class="breadcrumb-item"><a href="./">Home</a></li><li class="breadcrumb-item active" aria-current="page">{escape(current)}</li></ol></nav>
        <h1>{escape(title)}</h1><p class="mb-0">{intro}</p>
      </div>
    </section>"""


cta = """
    <section class="section-pad-sm"><div class="container"><div class="cta-panel"><div class="row align-items-center g-4"><div class="col-lg-8"><span class="section-kicker eyebrow-light">Connect with GRAIN</span><h2 class="section-title mb-2">Have an idea worth exploring?</h2><p class="mb-0">Start a conversation about research, project development or innovation.</p></div><div class="col-lg-4 text-lg-end"><a class="btn btn-gold" href="contact.html">Contact our team <i class="bi bi-arrow-up-right" aria-hidden="true"></i></a></div></div></div></div></section>"""


home = """
<section class="hero">
  <div class="container"><div class="row align-items-center g-3">
    <div class="col-lg-7"><div class="hero-content"><span class="section-kicker eyebrow-light">Global Research, Advisory and Innovation Network</span><h1>From scholarship<br> to <em>enterprise.</em></h1><p>GRAIN connects African scholars and researchers across the world with the development challenges of their continent — bringing research, advisory expertise and innovation closer to practical solutions.</p><div class="d-flex flex-wrap gap-3 mt-4"><a class="btn btn-gold" href="our-organization.html">Discover GRAIN <i class="bi bi-arrow-up-right" aria-hidden="true"></i></a><a class="btn btn-outline-light-custom" href="contact.html">Start a conversation <i class="bi bi-arrow-right" aria-hidden="true"></i></a></div></div></div>
    <div class="col-lg-5"><div class="hero-visual"><img class="main-photo" src="assets/images/research-lab.jpg" alt="Illustrative photograph of a researcher working at a microscope" width="2000" height="1125" fetchpriority="high"><img class="small-photo" src="assets/images/collaboration.jpg" alt="Illustrative photograph of professionals in discussion" width="2000" height="1333"><div class="circle-seal" aria-hidden="true">Research<br>Ideas<br>Impact</div><div class="visual-caption">Rooted in Africa. Connected to knowledge across the world.</div></div></div>
  </div></div>
  <div class="hero-bottom py-3"><div class="container">Research <span class="dot">✦</span> Advisory <span class="dot">✦</span> Innovation</div></div>
</section>
<section class="overlap-cards pb-5" aria-label="GRAIN work streams"><div class="container"><div class="row g-4">
  <div class="col-md-4"><article class="work-card"><span class="icon-tile"><i class="bi bi-journal-richtext" aria-hidden="true"></i></span><h2>Research & knowledge</h2><p>Connect scholars around development questions and help credible evidence reach the people who can use it.</p><a class="text-link" href="our-organization.html#how-we-work">Explore the approach <i class="bi bi-arrow-right" aria-hidden="true"></i></a></article></div>
  <div class="col-md-4"><article class="work-card"><span class="icon-tile"><i class="bi bi-compass" aria-hidden="true"></i></span><h2>Advisory & projects</h2><p>Bring research into feasibility, strategy and project preparation for institutions and partners.</p><a class="text-link" href="our-organization.html#how-we-work">Explore the approach <i class="bi bi-arrow-right" aria-hidden="true"></i></a></article></div>
  <div class="col-md-4"><article class="work-card"><span class="icon-tile"><i class="bi bi-lightbulb" aria-hidden="true"></i></span><h2>Innovation & enterprise</h2><p>Build the skills and connections that can help promising ideas become practical ventures.</p><a class="text-link" href="our-organization.html#how-we-work">Explore the approach <i class="bi bi-arrow-right" aria-hidden="true"></i></a></article></div>
</div></div></section>
<section class="section-pad"><div class="container"><div class="row align-items-center g-5"><div class="col-lg-6"><div class="image-frame"><img src="assets/images/research-insights.jpg" alt="Illustrative photograph of a researcher reviewing charts on a laptop" width="2000" height="1333" loading="lazy"><span class="image-label">Knowledge in action</span></div></div><div class="col-lg-6 ps-lg-5"><span class="section-kicker">Why GRAIN</span><h2 class="section-title">A network built around useful knowledge.</h2><p class="lead-copy">Africa's scholars produce ideas with the potential to improve lives and strengthen institutions. GRAIN is being developed to help those ideas travel further — from research questions to evidence, and from evidence to projects that can be tested and grown.</p><ul class="simple-list"><li><i class="bi bi-check-circle-fill" aria-hidden="true"></i><span>Research informed by Africa's development priorities.</span></li><li><i class="bi bi-check-circle-fill" aria-hidden="true"></i><span>Collaboration across scholarship, public institutions and industry.</span></li><li><i class="bi bi-check-circle-fill" aria-hidden="true"></i><span>A pathway from knowledge to practical application.</span></li></ul><a class="btn btn-grain" href="our-organization.html">More about GRAIN <i class="bi bi-arrow-up-right" aria-hidden="true"></i></a></div></div></div></section>
<section class="quote-band"><div class="container"><div class="row"><div class="col-lg-10"><span class="quote-mark" aria-hidden="true">“</span><blockquote>A continent built by its own scholars.</blockquote><p class="mt-3 mb-0 fw-bold text-uppercase" style="letter-spacing:.12em;font-size:.75rem">GRAIN vision · 2026–2027 strategic direction</p></div></div></div></section>
<section class="section-pad pale-section"><div class="container"><div class="row align-items-end mb-4 g-3"><div class="col-lg-8"><span class="section-kicker">Our model</span><h2 class="section-title mb-0">Connect. Develop. Apply.</h2></div><div class="col-lg-4 text-lg-end"><a class="text-link" href="our-organization.html#how-we-work">How the network works <i class="bi bi-arrow-right" aria-hidden="true"></i></a></div></div><div class="row g-4"><div class="col-md-4"><div class="topic-card"><span class="number">01 / CONNECT</span><h3>Bring knowledge together</h3><p>Build relationships between African scholars, universities, industry and institutions across regions.</p></div></div><div class="col-md-4"><div class="topic-card"><span class="number">02 / DEVELOP</span><h3>Strengthen ideas</h3><p>Shape research and concepts through mentoring, evidence and practical project thinking.</p></div></div><div class="col-md-4"><div class="topic-card"><span class="number">03 / APPLY</span><h3>Move toward impact</h3><p>Connect strong ideas with the partners and pathways needed for decisions, projects and enterprise.</p></div></div></div></div></section>
<section class="section-pad"><div class="container"><div class="row align-items-end g-3 mb-4"><div class="col-lg-8"><span class="section-kicker">In the community</span><h2 class="section-title mb-0">Events & conversations</h2></div><div class="col-lg-4 text-lg-end"><a class="text-link" href="events.html">Explore all events <i class="bi bi-arrow-right" aria-hidden="true"></i></a></div></div><div class="feature-event"><div class="row g-0 align-items-center"><div class="col-lg-6"><img src="assets/images/summit-stage.jpg" alt="Speakers on stage at the 2026 Entrepreneurship, Innovation and Startup Success Summit" width="1024" height="768" loading="lazy"></div><div class="col-lg-6"><div class="feature-copy"><span class="grain-tag gold">Past event · August 2026</span><h3 class="mt-4 mb-3" style="font-size:clamp(1.9rem,3vw,2.8rem)">Entrepreneurship, Innovation & Startup Success Summit</h3><p>The summit in Herne, Germany brought together conversations on ideas, enterprise and impact. Its programme listed GRAIN among the sponsors.</p><a class="btn btn-gold mt-2" href="event-startup-summit.html">Explore event <i class="bi bi-arrow-up-right" aria-hidden="true"></i></a></div></div></div></div></div></section>
<section class="section-pad pale-section"><div class="container"><div class="row align-items-end g-3 mb-4"><div class="col-lg-8"><span class="section-kicker">News & updates</span><h2 class="section-title mb-0">What we're thinking about</h2></div><div class="col-lg-4 text-lg-end"><a class="text-link" href="news.html">View all updates <i class="bi bi-arrow-right" aria-hidden="true"></i></a></div></div><div class="row g-4"><div class="col-lg-6"><article class="news-card"><img src="assets/images/research-detail.jpg" alt="Illustrative image of a magnifying glass and books" width="2000" height="1121" loading="lazy"><div class="card-body"><span class="grain-tag">Strategic direction</span><h3 class="mt-3"><a class="text-decoration-none" href="news-direction.html">From scholarship to enterprise: GRAIN's direction</a></h3><p class="mb-3">The network's strategic direction links research excellence with advisory work and pathways for innovation.</p><a class="text-link" href="news-direction.html">Read the story <i class="bi bi-arrow-right" aria-hidden="true"></i></a></div></article></div><div class="col-lg-6"><article class="news-card"><img src="assets/images/summit-group.jpg" alt="Participants at the 2026 Entrepreneurship, Innovation and Startup Success Summit" width="1024" height="768" loading="lazy"><div class="card-body"><span class="grain-tag gold">Event note</span><h3 class="mt-3"><a class="text-decoration-none" href="event-startup-summit.html">GRAIN on the 2026 summit programme</a></h3><p class="mb-3">The event poster listed GRAIN as a sponsor and its coordinator among speakers at the Herne gathering.</p><a class="text-link" href="event-startup-summit.html">Explore event <i class="bi bi-arrow-right" aria-hidden="true"></i></a></div></article></div></div></div></section>
""" + cta


organization = inner_hero("Our Organization", "Connecting African scholarship with research, advisory and innovation pathways.", "Our Organization") + """
<section class="section-pad"><div class="container"><div class="row align-items-center g-5"><div class="col-lg-6"><span class="section-kicker">Our purpose</span><h2 class="section-title">Why GRAIN exists</h2><p class="lead-copy">Important development questions rarely fit within one discipline or institution. GRAIN's model brings researchers and partners together to define useful questions, produce credible evidence and turn findings into decisions, projects and enterprises.</p><p>Our focus is work that responds to African priorities while drawing on knowledge from a worldwide community of scholars and professionals.</p></div><div class="col-lg-6"><div class="image-frame"><img src="assets/images/collaboration.jpg" alt="Illustrative image of professionals discussing ideas" width="2000" height="1333"><span class="image-label">Across disciplines</span></div></div></div></div></section>
<section class="section-pad pale-section"><div class="container"><div class="row g-4"><div class="col-lg-5"><span class="section-kicker">What guides us</span><h2 class="section-title">A clear purpose for research and innovation.</h2><p>The written 2026–2027 strategic direction sets out a vision and mission centred on African scholarship and practical application.</p></div><div class="col-lg-7"><div class="stats-ribbon mb-3"><span class="grain-tag gold">Our vision</span><h3 class="mt-3 mb-0" style="font-size:1.7rem">A continent built by its own scholars.</h3></div><div class="stats-ribbon"><span class="grain-tag">Our mission</span><p class="mb-0 mt-3">GRAIN connects African scholars and researchers across the world to the development challenges of their continent — building their entrepreneurial capacities, converting their research into bankable projects, and sustaining them as founders and innovators who build from wherever they stand.</p></div></div></div></div></section>
<section class="section-pad" id="how-we-work"><div class="container"><div class="row mb-4"><div class="col-lg-9"><span class="section-kicker">How we work</span><h2 class="section-title">One network, connected stages of work.</h2><p class="lead-copy">The strategy describes a coordinating centre and regional chapter model that can bring together scholarship, industry, public institutions and development partners.</p></div></div><div class="row g-4"><div class="col-md-4"><div class="flow-step"><span class="step-number">01 / RESEARCH</span><h3>Generate useful evidence</h3><p>Frame relevant questions, strengthen research quality and make knowledge easier to find and use.</p></div></div><div class="col-md-4"><div class="flow-step"><span class="step-number">02 / ADVISORY</span><h3>Shape decisions and projects</h3><p>Apply evidence to strategy, feasibility and project development with suitable partners.</p></div></div><div class="col-md-4"><div class="flow-step"><span class="step-number">03 / INNOVATION</span><h3>Build routes to enterprise</h3><p>Help promising concepts advance through entrepreneurial learning and practical collaboration.</p></div></div></div><div class="notice-box mt-5"><strong>Developing network:</strong> chapter locations, partner lists and programme enrolment will be added as they are formally confirmed.</div></div></section>
<section class="section-pad pale-section"><div class="container"><div class="row mb-4"><div class="col-lg-8"><span class="section-kicker">Our values</span><h2 class="section-title mb-0">Principles behind the work</h2></div></div><div class="row g-3"><div class="col-md-6 col-lg-4"><div class="value-card"><span class="value-number">01</span><h3>Research excellence</h3><p>Rigour, integrity and evidence that decision makers can use.</p></div></div><div class="col-md-6 col-lg-4"><div class="value-card"><span class="value-number">02</span><h3>Innovation with purpose</h3><p>Ideas that respond to real problems and can be tested in practice.</p></div></div><div class="col-md-6 col-lg-4"><div class="value-card"><span class="value-number">03</span><h3>Collaborative leadership</h3><p>Shared work across disciplines, institutions and regions.</p></div></div><div class="col-md-6 col-lg-4"><div class="value-card"><span class="value-number">04</span><h3>Inclusion and diversity</h3><p>Room for the voices and experiences of the communities served.</p></div></div><div class="col-md-6 col-lg-4"><div class="value-card"><span class="value-number">05</span><h3>Accountability and transparency</h3><p>Clarity about evidence, resources, decisions and results.</p></div></div><div class="col-md-6 col-lg-4"><div class="value-card"><span class="value-number">06</span><h3>Pan-African ambition</h3><p>A global network with Africa's development needs at its centre.</p></div></div></div></div></section>
""" + cta


events = inner_hero("Events", "Research advances when people share ideas. Explore GRAIN's documented event participation and future announcements.", "Events") + """
<section class="section-pad"><div class="container"><div class="row align-items-end g-3 mb-4"><div class="col-lg-8"><span class="section-kicker">Event archive</span><h2 class="section-title mb-0">Recent conversations</h2></div><div class="col-lg-4 text-lg-end"><span class="grain-tag">Past events</span></div></div><div class="row g-4">
  <div class="col-lg-6"><article class="event-card"><img src="assets/images/summit-stage.jpg" alt="Stage presentation at the 2026 Entrepreneurship, Innovation and Startup Success Summit" width="1024" height="768"><div class="card-body"><div class="meta mb-2"><i class="bi bi-calendar3 me-2" aria-hidden="true"></i>14–15 August 2026 <span class="mx-2">·</span> Herne, Germany</div><h3>Entrepreneurship, Innovation & Startup Success Summit 2026</h3><p>The programme listed GRAIN among the sponsors and its coordinator among the speakers.</p><a class="text-link" href="event-startup-summit.html">View event details <i class="bi bi-arrow-right" aria-hidden="true"></i></a></div></article></div>
  <div class="col-lg-6"><article class="event-card"><img class="poster-crop" src="assets/images/grasag-poster.jpg" alt="Poster for the 3rd GRASAG-USA Annual Congress" width="647" height="733"><div class="card-body"><div class="meta mb-2"><i class="bi bi-calendar3 me-2" aria-hidden="true"></i>23–26 July 2026 <span class="mx-2">·</span> Maryland, USA</div><h3>3rd GRASAG-USA Annual Congress</h3><p>The congress poster listed Dr Rebecca Yandam, Coordinator of the GRAIN Project, as a guest speaker.</p><a class="text-link" href="event-grasag-congress.html">View event details <i class="bi bi-arrow-right" aria-hidden="true"></i></a></div></article></div>
</div></div></section>
<section class="section-pad pale-section"><div class="container"><div class="row align-items-center g-4"><div class="col-lg-8"><span class="section-kicker">Looking ahead</span><h2 class="section-title mb-2">Upcoming events</h2><p class="mb-0">New event dates and registration details will appear here once confirmed. The strategic plan proposes research forums, symposia and chapter conversations as the network develops.</p></div><div class="col-lg-4 text-lg-end"><a class="btn btn-grain" href="contact.html">Ask about events <i class="bi bi-arrow-up-right" aria-hidden="true"></i></a></div></div></div></section>
"""


news = inner_hero("News & Updates", "Ideas, conversations and programme notes from across GRAIN's developing network.", "News & Updates") + """
<section class="section-pad"><div class="container"><div class="row mb-4"><div class="col-lg-9"><span class="section-kicker">In focus</span><h2 class="section-title">Current notes</h2><p class="lead-copy">This holding site begins with GRAIN's documented strategic direction and an event note. More news will be added when announcements, research outputs and programme details are confirmed.</p></div></div><div class="row g-4">
  <div class="col-lg-6"><article class="news-card"><img src="assets/images/research-detail.jpg" alt="Illustrative photograph of books and a magnifying glass" width="2000" height="1121"><div class="card-body"><span class="grain-tag">Strategic direction</span><h3 class="mt-3"><a class="text-decoration-none" href="news-direction.html">From scholarship to enterprise: GRAIN's direction</a></h3><p>The 2026–2027 direction describes how research, advisory work and innovation can form a connected pathway.</p><a class="text-link" href="news-direction.html">Read more <i class="bi bi-arrow-right" aria-hidden="true"></i></a></div></article></div>
  <div class="col-lg-6"><article class="news-card"><img src="assets/images/summit-group.jpg" alt="Participants at the 2026 Entrepreneurship, Innovation and Startup Success Summit" width="1024" height="768"><div class="card-body"><span class="grain-tag gold">Event note</span><h3 class="mt-3"><a class="text-decoration-none" href="event-startup-summit.html">GRAIN on the summit programme in Herne</a></h3><p>The summit programme listed GRAIN as a sponsor at the August 2026 gathering in Germany.</p><a class="text-link" href="event-startup-summit.html">Explore event <i class="bi bi-arrow-right" aria-hidden="true"></i></a></div></article></div>
</div></div></section>
<section class="section-pad pale-section"><div class="container"><div class="row mb-4"><div class="col-lg-8"><span class="section-kicker">What to expect</span><h2 class="section-title mb-0">Updates with a clear source.</h2></div></div><div class="row g-4"><div class="col-md-4"><div class="topic-card"><span class="icon-tile"><i class="bi bi-file-earmark-text" aria-hidden="true"></i></span><h3>Research</h3><p>New findings and knowledge products when they are reviewed and released.</p></div></div><div class="col-md-4"><div class="topic-card"><span class="icon-tile"><i class="bi bi-people" aria-hidden="true"></i></span><h3>Events</h3><p>Confirmed convenings, speaker participation and concise recaps.</p></div></div><div class="col-md-4"><div class="topic-card"><span class="icon-tile"><i class="bi bi-lightbulb" aria-hidden="true"></i></span><h3>Opportunities</h3><p>Calls and ways to participate after eligibility and deadlines are approved.</p></div></div></div></div></section>
""" + cta


contact = inner_hero("Contact Us", "Start a conversation about research, advisory, innovation or an event.", "Contact Us") + f"""
<section class="section-pad"><div class="container"><div class="row g-4 mb-5"><div class="col-md-6"><div class="contact-card"><span class="contact-icon"><i class="bi bi-envelope" aria-hidden="true"></i></span><h2>Email GRAIN</h2><p>Send your question or collaboration idea to our inbox.</p><a href="mailto:{EMAIL}">{EMAIL} <i class="bi bi-arrow-up-right" aria-hidden="true"></i></a></div></div><div class="col-md-6"><div class="contact-card"><span class="contact-icon"><i class="bi bi-telephone" aria-hidden="true"></i></span><h2>Call GRAIN</h2><p>Use the published contact number to reach the team.</p><a href="tel:{PHONE_LINK}">{PHONE_DISPLAY} <i class="bi bi-arrow-up-right" aria-hidden="true"></i></a></div></div></div><div class="row g-5 align-items-start"><div class="col-lg-5"><span class="section-kicker">Send an enquiry</span><h2 class="section-title">Tell us what you are working on.</h2><p class="lead-copy">Share a research question, project concept or collaboration idea. This holding site prepares an email in your own email application.</p><div class="notice-box"><strong>How this form works:</strong> your message is not stored by this website. After you select “Open email app,” review the prepared message and press Send in your email application.</div></div><div class="col-lg-7"><div class="form-shell"><form data-email-form data-destination="{EMAIL}" novalidate><div class="row g-3"><div class="col-md-6"><label class="form-label" for="name">Full name *</label><input class="form-control" id="name" name="name" autocomplete="name" required></div><div class="col-md-6"><label class="form-label" for="email">Email address *</label><input class="form-control" id="email" name="email" type="email" autocomplete="email" required></div><div class="col-md-6"><label class="form-label" for="organization">Organization</label><input class="form-control" id="organization" name="organization" autocomplete="organization"></div><div class="col-md-6"><label class="form-label" for="topic">Enquiry type *</label><select class="form-select" id="topic" name="topic" required><option value="" selected disabled>Select a topic</option><option>Research</option><option>Advisory</option><option>Innovation</option><option>Events</option><option>Media</option><option>Other</option></select></div><div class="col-12"><label class="form-label" for="message">Message *</label><textarea class="form-control" id="message" name="message" required></textarea></div><div class="col-12"><p class="form-note mb-2">* Required. Your email application handles delivery when you choose to send.</p><button class="btn btn-grain" type="submit">Open email app <i class="bi bi-arrow-up-right" aria-hidden="true"></i></button><div class="form-feedback" data-form-feedback></div></div></div></form><noscript><p class="form-note mt-3">JavaScript is needed to prepare the message. You can email <a href="mailto:{EMAIL}">{EMAIL}</a> directly.</p></noscript></div></div></div></div></section>
"""


summit = inner_hero("Startup Success Summit 2026", "A past event in Herne, Germany, focused on entrepreneurship, innovation and sustainable enterprise.", "Event Details") + """
<section class="section-pad"><div class="container"><div class="row g-5"><div class="col-lg-8"><img class="detail-cover" src="assets/images/summit-stage.jpg" alt="Presentation at the 2026 Entrepreneurship, Innovation and Startup Success Summit" width="1024" height="768"><div class="detail-body"><span class="grain-tag gold mt-4">Past event</span><h2>Turning ideas into impact</h2><p>The Entrepreneurship, Innovation & Startup Success Summit took place in Herne, Germany, on 14–15 August 2026. Its programme placed entrepreneurship, innovation and sustainable enterprise at the centre of the conversation.</p><p>The supplied programme poster lists GRAIN among the sponsors and Rebecca Yandam, identified there as GRAIN Coordinator, among the speakers. This page records that documented programme listing; a fuller account of GRAIN's contribution can be added when confirmed by the event team.</p><img class="img-fluid rounded mt-3" src="assets/images/summit-group.jpg" alt="Participants photographed at the 2026 summit" width="1024" height="768" loading="lazy"><p class="muted-small mt-2">Event photographs supplied in the GRAIN website folder.</p></div></div><div class="col-lg-4"><aside class="detail-panel" aria-label="Event facts"><span class="grain-tag">Event facts</span><dl><dt>Date</dt><dd>14–15 August 2026</dd><dt>Location</dt><dd>Herne, Germany</dd><dt>GRAIN role</dt><dd>Listed sponsor and speaker participation</dd><dt>Source</dt><dd>Supplied summit poster and event photographs</dd></dl><hr><a class="text-link" href="events.html">All events <i class="bi bi-arrow-right" aria-hidden="true"></i></a></aside><img class="img-fluid rounded mt-4" src="assets/images/summit-poster.jpg" alt="Summit poster listing speakers and sponsors" width="1131" height="1600" loading="lazy"></div></div></div></section>
""" + cta


grasag = inner_hero("3rd GRASAG-USA Annual Congress", "A congress programme listing a GRAIN Project guest speaker.", "Event Details") + """
<section class="section-pad"><div class="container"><div class="row g-5"><div class="col-lg-8"><div class="detail-body"><span class="grain-tag gold">Past event · Programme listing</span><h2 class="mt-4">Honoring our roots, building our future</h2><p>The 3rd GRASAG-USA Annual Congress was listed for 23–26 July 2026 at the University of Maryland, College Park. Its theme was “Honoring Our Roots, Building Our Future, And Advancing Ghanaian Global Impact.”</p><p>The supplied poster names Dr Rebecca Yandam as a guest speaker and identifies her as Head of Research at Zoomlion Ghana Limited and Coordinator of the GRAIN Project. A recap of her presentation can be added after the speaker or organizer verifies the details.</p><a class="btn btn-grain mt-3" href="events.html">Back to events <i class="bi bi-arrow-left" aria-hidden="true"></i></a></div></div><div class="col-lg-4"><aside class="detail-panel mb-4" aria-label="Event facts"><span class="grain-tag">Event facts</span><dl><dt>Date</dt><dd>23–26 July 2026</dd><dt>Location</dt><dd>University of Maryland, College Park, USA</dd><dt>GRAIN connection</dt><dd>Guest-speaker listing on poster</dd><dt>Source</dt><dd>Supplied congress poster</dd></dl></aside><img class="img-fluid rounded" src="assets/images/grasag-poster.jpg" alt="Poster for the 3rd GRASAG-USA Annual Congress" width="647" height="733"></div></div></div></section>
"""


direction = inner_hero("From scholarship to enterprise", "An introduction to the ideas in GRAIN's 2026–2027 strategic direction.", "Strategic Direction") + """
<article class="section-pad"><div class="container"><div class="row g-5"><div class="col-lg-8"><img class="detail-cover" src="assets/images/research-detail.jpg" alt="Illustrative photograph of books viewed through a magnifying glass" width="2000" height="1121"><div class="detail-body"><span class="grain-tag mt-4">Strategic direction</span><h2>Research with a path to application</h2><p>GRAIN's 2026–2027 strategic direction starts with the idea that African scholarship should have practical routes into policy, projects and enterprise. It describes a network that connects researchers across the world to the development challenges of their continent.</p><p>In that model, research is the starting point. Strong evidence can inform advisory work, help shape projects and give promising innovations a more realistic route to implementation. The plan also emphasizes entrepreneurial capacity, collaboration between institutions and industry, and careful stewardship of research outputs.</p><h2>What comes next</h2><p>The strategy proposes a coordinating centre, regional chapters, a knowledge platform and convenings for researchers and partners. These are development priorities. Individual programmes and participation routes will be announced here when their details are confirmed.</p><p>The written vision is “A continent built by its own scholars.” Its guiding line is “From scholarship to enterprise.”</p></div></div><div class="col-lg-4"><aside class="detail-panel"><span class="grain-tag">Source note</span><p class="mt-3">This article summarizes the <em>GRAIN GCC Strategic Direction and Action Plan 2026–2027</em> supplied for website development. It describes planned work and does not report programme delivery.</p><a class="text-link" href="news.html">All updates <i class="bi bi-arrow-right" aria-hidden="true"></i></a></aside></div></div></div></article>
""" + cta


pages = [
    ("index.html", "GRAIN | Global Research, Advisory and Innovation Network", "GRAIN connects African scholars and researchers with pathways from research to advisory work, innovation and enterprise.", "home", home),
    ("our-organization.html", "Our Organization | GRAIN", "Explore GRAIN's vision, mission and model for connecting African scholarship with practical development work.", "organization", organization),
    ("events.html", "Events | GRAIN", "Explore GRAIN event participation and announced opportunities to connect around research and innovation.", "events", events),
    ("news.html", "News & Updates | GRAIN", "Read GRAIN programme notes, event updates and the ideas shaping its research and innovation network.", "news", news),
    ("contact.html", "Contact Us | GRAIN", "Contact GRAIN about research, advisory work, innovation, events and collaboration.", "contact", contact),
    ("event-startup-summit.html", "Startup Success Summit 2026 | GRAIN Events", "Read about the Entrepreneurship, Innovation and Startup Success Summit 2026 in Herne, Germany.", "events", summit),
    ("event-grasag-congress.html", "3rd GRASAG-USA Annual Congress | GRAIN Events", "Review the GRAIN Project guest-speaker listing for the 3rd GRASAG-USA Annual Congress.", "events", grasag),
    ("news-direction.html", "From Scholarship to Enterprise | GRAIN", "Learn how GRAIN's 2026–2027 strategic direction connects research, advisory work and innovation.", "news", direction),
]

for args in pages:
    layout(*args)
print(f"Generated {len(pages)} HTML pages in {ROOT}")
