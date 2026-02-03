# aaronjl86.github.io
[DidYouHearNewport.html](https://github.com/user-attachments/files/25044421/DidYouHearNewport.html)
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Did You Hear Newport</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background: #f9f9f9; }
        .container { max-width: 1200px; margin: 0 auto; padding: 0 20px; }

        /* Navigation */
        nav { position: fixed; top: 0; left: 0; right: 0; background: white; border-bottom: 1px solid #e0e0e0; z-index: 50; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
        nav .nav-inner { display: flex; justify-content: space-between; align-items: center; padding: 15px 0; }
        nav .logo { font-size: 18px; font-weight: bold; color: #001F3F; }
        nav .nav-links { display: none; gap: 30px; }
        nav .nav-links.show { display: flex; }
        nav button { background: none; border: none; cursor: pointer; font-size: 20px; }
        nav a { text-decoration: none; color: #333; font-weight: 500; cursor: pointer; transition: color 0.2s; }
        nav a:hover { color: #FF6B35; }
        nav a.active { color: #FF6B35; }

        @media (min-width: 768px) {
            nav .nav-links { display: flex !important; }
            nav button { display: none; }
        }

        /* Main Content */
        main { padding-top: 80px; }

        /* Hero */
        .hero { background: linear-gradient(135deg, #f9f9f9, #f0f4ff); padding: 80px 0; text-align: center; }
        .hero h1 { font-size: 56px; color: #001F3F; margin-bottom: 20px; line-height: 1.2; }
        .hero h1 .highlight { color: #FF6B35; }
        .hero p { font-size: 20px; color: #666; max-width: 600px; margin: 0 auto 40px; line-height: 1.6; }

        /* Form */
        .signup-form { max-width: 500px; margin: 0 auto 30px; }
        .form-group { display: flex; gap: 10px; flex-direction: column; }
        @media (min-width: 640px) {
            .form-group { flex-direction: row; }
        }
        .form-group input { flex: 1; padding: 15px; border: 2px solid #ddd; border-radius: 8px; font-size: 16px; }
        .form-group input:focus { outline: none; border-color: #FF6B35; }
        .form-group button { padding: 15px 30px; background: #FF6B35; color: white; border: none; border-radius: 8px; font-weight: bold; cursor: pointer; transition: background 0.2s; }
        .form-group button:hover { background: #e55a25; }
        .form-note { font-size: 14px; color: #999; margin-top: 10px; }

        .trust-signal { font-size: 14px; color: #999; margin-bottom: 40px; }

        /* Three Pillars */
        .pillars { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 30px; margin: 60px 0; }
        .pillar { background: white; padding: 30px; border-radius: 12px; border: 1px solid #e0e0e0; transition: border-color 0.2s; }
        .pillar:hover { border-color: #FF6B35; }
        .pillar-icon { font-size: 40px; margin-bottom: 15px; }
        .pillar h3 { color: #001F3F; margin-bottom: 10px; font-size: 18px; }
        .pillar p { color: #666; line-height: 1.6; }

        /* Why Section */
        .why-section { background: #001F3F; color: white; padding: 60px 0; margin: 60px 0; border-radius: 16px; }
        .why-section h2 { font-size: 36px; text-align: center; margin-bottom: 40px; }
        .why-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 30px; }
        .why-item { display: flex; gap: 20px; }
        .why-number { color: #FF6B35; font-size: 24px; font-weight: bold; flex-shrink: 0; }
        .why-item h3 { color: white; margin-bottom: 10px; font-size: 16px; }
        .why-item p { color: #b0d4ff; line-height: 1.6; font-size: 14px; }

        /* Posts Page */
        .posts-grid { display: grid; gap: 20px; margin: 40px 0; }
        .post { background: white; padding: 30px; border-radius: 12px; border: 1px solid #e0e0e0; cursor: pointer; transition: all 0.2s; }
        .post:hover { border-color: #FF6B35; box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
        .post-meta { display: flex; justify-content: space-between; gap: 20px; margin-bottom: 15px; flex-wrap: wrap; }
        .post-category { font-size: 12px; font-weight: bold; color: #FF6B35; text-transform: uppercase; }
        .post-date { font-size: 12px; color: #999; }
        .post h3 { color: #001F3F; margin-bottom: 15px; font-size: 22px; }
        .post p { color: #666; line-height: 1.6; margin-bottom: 15px; }
        .post-footer { display: flex; justify-content: space-between; border-top: 1px solid #e0e0e0; padding-top: 15px; font-size: 14px; color: #999; }
        .post-footer span { color: #FF6B35; }

        /* About Page */
        .about-content { max-width: 800px; margin: 40px auto; }
        .about-content h3 { color: #001F3F; margin-top: 30px; margin-bottom: 15px; font-size: 20px; }
        .about-content p { color: #666; line-height: 1.8; margin-bottom: 15px; }
        .about-content ul { margin-left: 20px; }
        .about-content li { color: #666; line-height: 1.8; margin-bottom: 10px; }
        .about-cta { background: #f0f4ff; border: 2px solid #001F3F; padding: 30px; border-radius: 12px; text-align: center; margin: 40px 0; }
        .about-cta p { color: #001F3F; font-size: 18px; font-weight: bold; margin-bottom: 15px; }
        .about-cta button { padding: 15px 30px; background: #FF6B35; color: white; border: none; border-radius: 8px; font-weight: bold; cursor: pointer; }

        /* Footer */
        footer { background: #001F3F; color: #b0d4ff; padding: 40px 0; margin-top: 60px; }
        footer .footer-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 30px; margin-bottom: 30px; }
        footer h4 { color: white; margin-bottom: 15px; }
        footer p { font-size: 14px; line-height: 1.6; }
        footer .footer-bottom { border-top: 1px solid #1a3a5a; padding-top: 30px; text-align: center; font-size: 14px; }

        /* Pages */
        .page { display: none; }
        .page.active { display: block; }

        h1, h2, h3 { margin: 0; }
        button { cursor: pointer; }
    </style>
</head>
<body>
    <!-- Navigation -->
    <nav>
        <div class="container nav-inner">
            <div class="logo">Did You Hear Newport</div>
            <div class="nav-links">
                <a onclick="showPage('home')" class="nav-link active">Home</a>
                <a onclick="showPage('posts')" class="nav-link">Posts</a>
                <a onclick="showPage('about')" class="nav-link">About</a>
            </div>
            <button onclick="toggleMenu()">☰</button>
        </div>
    </nav>

    <main>
        <!-- Home Page -->
        <div id="home" class="page active">
            <section class="hero">
                <div class="container">
                    <h1>What Are People <span class="highlight">Actually Talking About</span> in Newport?</h1>
                    <p>Early-signal local news from your community. Before it's official. Before it's everywhere. Just real intelligence from Newport residents, for Newport residents.</p>

                    <div class="signup-form">
                        <form onsubmit="handleSubscribe(event)">
                            <div class="form-group">
                                <input type="email" id="email" placeholder="Your email" required>
                                <button type="submit">Subscribe</button>
                            </div>
                        </form>
                        <p class="form-note">No spam. One email when something real happens. That's it.</p>
                    </div>

                    <div class="trust-signal">Join 500+ Newport residents who actually stay informed</div>
                </div>
            </section>

            <section>
                <div class="container pillars">
                    <div class="pillar">
                        <div class="pillar-icon">⚡</div>
                        <h3>Early Signal</h3>
                        <p>Catch what's being talked about before it becomes official news. Stay ahead.</p>
                    </div>
                    <div class="pillar">
                        <div class="pillar-icon">👥</div>
                        <h3>Community-Sourced</h3>
                        <p>What residents are already discussing gets documented, verified, contextualized.</p>
                    </div>
                    <div class="pillar">
                        <div class="pillar-icon">💬</div>
                        <h3>You Participate</h3>
                        <p>Vote on what matters. Share what you're hearing. Shape next week's coverage.</p>
                    </div>
                </div>
            </section>

            <section class="why-section">
                <div class="container">
                    <h2>Why Newport Residents Need This</h2>
                    <div class="why-grid">
                        <div class="why-item">
                            <div class="why-number">1</div>
                            <div>
                                <h3>You already talk about it</h3>
                                <p>Group chats, coffee conversations, neighborhood discussions. We just organize it.</p>
                            </div>
                        </div>
                        <div class="why-item">
                            <div class="why-number">2</div>
                            <div>
                                <h3>Official channels move slow</h3>
                                <p>City council meets once a month. Real decisions happen between meetings.</p>
                            </div>
                        </div>
                        <div class="why-item">
                            <div class="why-number">3</div>
                            <div>
                                <h3>Information is fragmented</h3>
                                <p>Same conversation happens in 10 different threads. We centralize it.</p>
                            </div>
                        </div>
                        <div class="why-item">
                            <div class="why-number">4</div>
                            <div>
                                <h3>You want to stay informed, not obsessed</h3>
                                <p>One quality email beats endless scrolling through chaotic group chats.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
        </div>

        <!-- Posts Page -->
        <div id="posts" class="page">
            <div class="container" style="padding: 40px 0;">
                <h2 style="font-size: 32px; color: #001F3F; margin-bottom: 30px;">Recent Intelligence</h2>

                <div class="posts-grid">
                    <div class="post">
                        <div class="post-meta">
                            <span class="post-category">Infrastructure</span>
                            <span class="post-date">Feb 2, 2025</span>
                        </div>
                        <h3>The Cliff Walk Expansion Everyone's Talking About</h3>
                        <p>Rumors are swirling about plans to extend the Cliff Walk further north. Here's what we're hearing.</p>
                        <div class="post-footer">
                            <span>47 Newport residents engaged</span>
                            <span>→</span>
                        </div>
                    </div>

                    <div class="post">
                        <div class="post-meta">
                            <span class="post-category">Development</span>
                            <span class="post-date">Jan 29, 2025</span>
                        </div>
                        <h3>Did You Know About the New Waterfront Development?</h3>
                        <p>Local developers are looking at waterfront property. We found out what's actually being considered.</p>
                        <div class="post-footer">
                            <span>62 Newport residents engaged</span>
                            <span>→</span>
                        </div>
                    </div>

                    <div class="post">
                        <div class="post-meta">
                            <span class="post-category">Education</span>
                            <span class="post-date">Jan 26, 2025</span>
                        </div>
                        <h3>School Board's Quiet Decision About District Boundaries</h3>
                        <p>Before it was announced officially, people were already talking. Here's what's changing.</p>
                        <div class="post-footer">
                            <span>84 Newport residents engaged</span>
                            <span>→</span>
                        </div>
                    </div>

                    <div class="post">
                        <div class="post-meta">
                            <span class="post-category">Community</span>
                            <span class="post-date">Jan 22, 2025</span>
                        </div>
                        <h3>The Restaurant Scene Shift Nobody's Confirmed Yet</h3>
                        <p>Multiple Newport restaurants are making moves. Our community intelligence has the details.</p>
                        <div class="post-footer">
                            <span>73 Newport residents engaged</span>
                            <span>→</span>
                        </div>
                    </div>
                </div>

                <div style="text-align: center; margin-top: 40px;">
                    <p style="color: #666; margin-bottom: 20px;">Want to see more like this delivered to your inbox?</p>
                    <button onclick="showPage('home')" style="padding: 15px 30px; background: #FF6B35; color: white; border: none; border-radius: 8px; font-weight: bold; font-size: 16px;">Subscribe Now</button>
                </div>
            </div>
        </div>

        <!-- About Page -->
        <div id="about" class="page">
            <div class="container about-content" style="padding: 40px 0;">
                <h2 style="font-size: 32px; color: #001F3F; margin-bottom: 30px;">About Did You Hear Newport</h2>

                <h3>What We Are</h3>
                <p>Did You Hear Newport is a community intelligence platform disguised as a newsletter. We document and investigate the things Newport residents are already talking about in group chats and conversations—before they become official stories.</p>

                <h3>What Makes Us Different</h3>
                <ul>
                    <li><strong>Community-sourced</strong> over institutional. We start with what residents are discussing, not press releases.</li>
                    <li><strong>Early signal</strong> before official announcements. By the time it hits traditional media, it's old news.</li>
                    <li><strong>Ruthless curation</strong> over volume. No daily digests. If it doesn't matter, it doesn't get sent.</li>
                    <li><strong>Participatory</strong>, not passive. You vote on what matters. You submit tips. You shape coverage.</li>
                    <li><strong>Authentic voice</strong> over corporate tone. We sound like friends in a group chat, not a newsletter.</li>
                </ul>

                <h3>Our Promise</h3>
                <p>One email. Only when something real is happening that people are actually talking about. High signal. No fluff. You're not reading about Newport; you're reading from Newport.</p>

                <div class="about-cta">
                    <p>Ready to stay informed before everyone else?</p>
                    <button onclick="showPage('home')">Subscribe to Did You Hear Newport</button>
                </div>
            </div>
        </div>
    </main>

    <!-- Footer -->
    <footer>
        <div class="container footer-grid">
            <div>
                <h4>Did You Hear Newport</h4>
                <p>Community intelligence for Newport residents, by Newport residents.</p>
            </div>
            <div>
                <h4>Powered By</h4>
                <p>Built on Beehiiv. Hosted on your custom domain. Completely independent.</p>
            </div>
            <div>
                <h4>Get In Touch</h4>
                <p>Tips? Questions? Reply directly to any newsletter issue.</p>
            </div>
        </div>
        <div class="footer-bottom">
            <p>© 2025 Did You Hear Newport. Built for Newport, by a Newporter.</p>
        </div>
    </footer>

    <script>
        function showPage(pageName) {
            // Hide all pages
            document.querySelectorAll('.page').forEach(page => {
                page.classList.remove('active');
            });

            // Show selected page
            document.getElementById(pageName).classList.add('active');

            // Update nav links
            document.querySelectorAll('.nav-link').forEach(link => {
                link.classList.remove('active');
            });
            event.target.classList.add('active');

            // Close mobile menu
            document.querySelector('.nav-links').classList.remove('show');

            // Scroll to top
            window.scrollTo(0, 0);
        }

        function toggleMenu() {
            document.querySelector('.nav-links').classList.toggle('show');
        }

        function handleSubscribe(event) {
            event.preventDefault();
            const email = document.getElementById('email').value;
            if (email) {
                // Opens Beehiiv signup
                window.open('https://www.beehiiv.com/subscribe/didyouhearnewport', '_blank');
                document.getElementById('email').value = '';
            }
        }

        // Set initial active nav link
        document.addEventListener('DOMContentLoaded', function() {
            document.querySelectorAll('.nav-link')[0].classList.add('active');
        });
    </script>
</body>
</html>
