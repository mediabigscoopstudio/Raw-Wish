import re

with open('template/main/index.html', 'r') as f:
    content = f.read()

# 1. More Than Beauty (Light Theme)
old_mtb = """<section class="more-than-beauty" style="background-color: #231C18; overflow: hidden;">
    <div class="row g-0">
        <div class="col-lg-5 d-flex align-items-center" style="padding: 10%;">
            <div class="fade-up" style="color: #F8F6F0;">
                <div class="text-uppercase mb-4" style="font-size: 0.6rem; letter-spacing: 0.15em; color: #8A7E78;">Our Philosophy</div>
                <h2 class="mb-4" style="font-family: var(--font-serif); font-size: clamp(3rem, 5vw, 5.5rem); line-height: 1.05; letter-spacing: -0.02em;">More Than<br>Beauty.</h2>
                <p class="mb-5" style="font-size: 0.85rem; line-height: 1.8; max-width: 400px; color: #BDB5B0;">
                    Self-care is a form of power. Rawwish products are made with real ingredients, real intention and a deep respect for you and the planet.
                </p>
                <a href="/about" class="text-uppercase text-decoration-none" style="color: #F8F6F0; font-size: 0.65rem; letter-spacing: 0.15em;">Our Story &rarr;</a>
            </div>
        </div>
        <div class="col-lg-7">
            <img src="/static/main/images/product_1.webp" alt="More Than Beauty" style="width: 100%; height: 100%; object-fit: cover; min-height: 500px;">
        </div>
    </div>
</section>"""

new_mtb = """<section class="more-than-beauty" style="background-color: #FFFFFF; overflow: hidden;">
    <div class="row g-0">
        <div class="col-lg-5 d-flex align-items-center" style="padding: 10%;">
            <div class="fade-up" style="color: #231C18;">
                <div class="text-uppercase mb-4" style="font-size: 0.6rem; letter-spacing: 0.15em; color: #8A7E78;">Our Philosophy</div>
                <h2 class="mb-4" style="font-family: var(--font-serif); font-size: clamp(3rem, 5vw, 5.5rem); line-height: 1.05; letter-spacing: -0.02em;">More Than<br>Beauty.</h2>
                <p class="mb-5" style="font-size: 0.85rem; line-height: 1.8; max-width: 400px; color: #5A524D;">
                    Self-care is a form of power. Rawwish products are made with real ingredients, real intention and a deep respect for you and the planet.
                </p>
                <a href="/about" class="text-uppercase text-decoration-none" style="color: #231C18; font-size: 0.65rem; letter-spacing: 0.15em; border-bottom: 1px solid #231C18; padding-bottom: 4px;">Our Story &rarr;</a>
            </div>
        </div>
        <div class="col-lg-7">
            <img src="/static/main/images/product_1.webp" alt="More Than Beauty" style="width: 100%; height: 100%; object-fit: cover; min-height: 500px;">
        </div>
    </div>
</section>"""

content = content.replace(old_mtb, new_mtb)

# 2. Ingredients That Care (No scroll on desktop, fixed layout/gap)
old_ing = """<!-- INGREDIENTS -->
<section class="ingredients-section py-5" style="background-color: #F9F7F2; overflow-x: hidden;">
    <div class="container-fluid py-5 px-lg-5">
        <div class="row align-items-center">
            <!-- Left Text -->
            <div class="col-lg-3 pe-lg-4 mb-5 mb-lg-0 fade-up">
                <div class="text-uppercase mb-4" style="font-size: 0.6rem; letter-spacing: 0.15em; color: #8A7E78;">Nature's Finest</div>
                <h2 class="mb-4" style="font-family: var(--font-serif); font-size: clamp(3rem, 5vw, 4.5rem); line-height: 1.05; color: #231C18; letter-spacing: -0.02em;">Ingredients<br>That Care.</h2>
                <p class="mb-5" style="font-size: 0.85rem; line-height: 1.8; color: #5A524D;">
                    Thoughtfully chosen, high-quality ingredients that are gentle, effective and good for your skin &mdash; and the planet.
                </p>
                <a href="/ingredients" class="text-uppercase text-decoration-none" style="color: #231C18; font-size: 0.65rem; letter-spacing: 0.15em; border-bottom: 1px solid #231C18; padding-bottom: 4px;">Explore Ingredients &rarr;</a>
            </div>
            
            <!-- Right Carousel -->
            <div class="col-lg-9 fade-up" style="transition-delay: 0.2s;">
                <div class="d-flex gap-4 overflow-auto pb-4" style="scrollbar-width: none; ms-overflow-style: none;">
                    
                    <div class="flex-shrink-0" style="width: 220px;">
                        <img src="/static/main/images/product_1.webp" alt="Coffee" style="width: 100%; height: 260px; object-fit: cover; margin-bottom: 0;">
                        <div style="background-color: #EBE5DB; padding: 12px 15px;">
                            <h4 class="mb-1" style="font-family: var(--font-serif); font-size: 1.1rem; color: #231C18;">Coffee</h4>
                            <p class="mb-0" style="font-size: 0.65rem; color: #5A524D;">Energises & revitalises</p>
                        </div>
                    </div>
                    
                    <div class="flex-shrink-0" style="width: 220px;">
                        <img src="/static/main/images/product_1.webp" alt="Rose" style="width: 100%; height: 260px; object-fit: cover; margin-bottom: 0;">
                        <div style="background-color: #EBE5DB; padding: 12px 15px;">
                            <h4 class="mb-1" style="font-family: var(--font-serif); font-size: 1.1rem; color: #231C18;">Rose</h4>
                            <p class="mb-0" style="font-size: 0.65rem; color: #5A524D;">Soothes & hydrates</p>
                        </div>
                    </div>

                    <div class="flex-shrink-0" style="width: 220px;">
                        <img src="/static/main/images/product_1.webp" alt="Shea Butter" style="width: 100%; height: 260px; object-fit: cover; margin-bottom: 0;">
                        <div style="background-color: #EBE5DB; padding: 12px 15px;">
                            <h4 class="mb-1" style="font-family: var(--font-serif); font-size: 1.1rem; color: #231C18;">Shea Butter</h4>
                            <p class="mb-0" style="font-size: 0.65rem; color: #5A524D;">Nourishes & repairs</p>
                        </div>
                    </div>

                    <div class="flex-shrink-0" style="width: 220px;">
                        <img src="/static/main/images/product_1.webp" alt="Aloe Vera" style="width: 100%; height: 260px; object-fit: cover; margin-bottom: 0;">
                        <div style="background-color: #EBE5DB; padding: 12px 15px;">
                            <h4 class="mb-1" style="font-family: var(--font-serif); font-size: 1.1rem; color: #231C18;">Aloe Vera</h4>
                            <p class="mb-0" style="font-size: 0.65rem; color: #5A524D;">Calms & heals</p>
                        </div>
                    </div>

                    <div class="flex-shrink-0" style="width: 220px;">
                        <img src="/static/main/images/product_1.webp" alt="Turmeric" style="width: 100%; height: 260px; object-fit: cover; margin-bottom: 0;">
                        <div style="background-color: #EBE5DB; padding: 12px 15px;">
                            <h4 class="mb-1" style="font-family: var(--font-serif); font-size: 1.1rem; color: #231C18;">Turmeric</h4>
                            <p class="mb-0" style="font-size: 0.65rem; color: #5A524D;">Brightens & protects</p>
                        </div>
                    </div>

                </div>
                <style>
                    .ingredients-section .d-flex::-webkit-scrollbar { display: none; }
                </style>
            </div>
        </div>
    </div>
</section>"""

new_ing = """<!-- INGREDIENTS -->
<section class="ingredients-section py-5" style="background-color: #F9F7F2; overflow-x: hidden;">
    <div class="container-fluid py-5 px-lg-5">
        <div class="row align-items-center">
            <!-- Left Text -->
            <div class="col-lg-3 pe-lg-5 mb-5 mb-lg-0 fade-up">
                <div class="text-uppercase mb-4" style="font-size: 0.6rem; letter-spacing: 0.15em; color: #8A7E78;">Nature's Finest</div>
                <h2 class="mb-4" style="font-family: var(--font-serif); font-size: clamp(3rem, 5vw, 4.5rem); line-height: 1.05; color: #231C18; letter-spacing: -0.02em;">Ingredients<br>That Care.</h2>
                <p class="mb-5" style="font-size: 0.85rem; line-height: 1.8; color: #5A524D;">
                    Thoughtfully chosen, high-quality ingredients that are gentle, effective and good for your skin &mdash; and the planet.
                </p>
                <a href="/ingredients" class="text-uppercase text-decoration-none" style="color: #231C18; font-size: 0.65rem; letter-spacing: 0.15em; border-bottom: 1px solid #231C18; padding-bottom: 4px;">Explore Ingredients &rarr;</a>
            </div>
            
            <!-- Right Grid -->
            <div class="col-lg-9 fade-up" style="transition-delay: 0.2s;">
                <div class="row row-cols-2 row-cols-md-3 row-cols-lg-5 g-3">
                    
                    <div class="col">
                        <img src="/static/main/images/product_1.webp" alt="Coffee" style="width: 100%; height: 180px; object-fit: cover; margin-bottom: 0;">
                        <div style="background-color: #EBE5DB; padding: 12px 15px;">
                            <h4 class="mb-1" style="font-family: var(--font-serif); font-size: 1rem; color: #231C18;">Coffee</h4>
                            <p class="mb-0" style="font-size: 0.6rem; color: #5A524D;">Energises & revitalises</p>
                        </div>
                    </div>
                    
                    <div class="col">
                        <img src="/static/main/images/product_1.webp" alt="Rose" style="width: 100%; height: 180px; object-fit: cover; margin-bottom: 0;">
                        <div style="background-color: #EBE5DB; padding: 12px 15px;">
                            <h4 class="mb-1" style="font-family: var(--font-serif); font-size: 1rem; color: #231C18;">Rose</h4>
                            <p class="mb-0" style="font-size: 0.6rem; color: #5A524D;">Soothes & hydrates</p>
                        </div>
                    </div>

                    <div class="col">
                        <img src="/static/main/images/product_1.webp" alt="Shea Butter" style="width: 100%; height: 180px; object-fit: cover; margin-bottom: 0;">
                        <div style="background-color: #EBE5DB; padding: 12px 15px;">
                            <h4 class="mb-1" style="font-family: var(--font-serif); font-size: 1rem; color: #231C18;">Shea Butter</h4>
                            <p class="mb-0" style="font-size: 0.6rem; color: #5A524D;">Nourishes & repairs</p>
                        </div>
                    </div>

                    <div class="col">
                        <img src="/static/main/images/product_1.webp" alt="Aloe Vera" style="width: 100%; height: 180px; object-fit: cover; margin-bottom: 0;">
                        <div style="background-color: #EBE5DB; padding: 12px 15px;">
                            <h4 class="mb-1" style="font-family: var(--font-serif); font-size: 1rem; color: #231C18;">Aloe Vera</h4>
                            <p class="mb-0" style="font-size: 0.6rem; color: #5A524D;">Calms & heals</p>
                        </div>
                    </div>

                    <div class="col">
                        <img src="/static/main/images/product_1.webp" alt="Turmeric" style="width: 100%; height: 180px; object-fit: cover; margin-bottom: 0;">
                        <div style="background-color: #EBE5DB; padding: 12px 15px;">
                            <h4 class="mb-1" style="font-family: var(--font-serif); font-size: 1rem; color: #231C18;">Turmeric</h4>
                            <p class="mb-0" style="font-size: 0.6rem; color: #5A524D;">Brightens & protects</p>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>
</section>"""

content = content.replace(old_ing, new_ing)


# 3. Good skin. Good rituals & Real Skin. Real Stories (Light Theme + Webm videos)
# We will use re.sub for this because the block is large and might have small formatting differences.
old_newsletter = """<!-- NEWSLETTER & INSTAGRAM -->
<section class="newsletter-instagram-section py-5" style="background-color: #1A1513; color: #F8F6F0;">
    <div class="container py-5">
        <!-- Newsletter Row -->
        <div class="row mb-5 align-items-center fade-up">
            <div class="col-lg-5">
                <div class="text-uppercase mb-3" style="font-size: 0.6rem; letter-spacing: 0.15em; color: #8A7E78;">Join The Rawwish Community</div>
                <h2 style="font-family: var(--font-serif); font-size: clamp(3rem, 5vw, 4.5rem); line-height: 1.05; margin-bottom: 0; letter-spacing: -0.02em;">Good skin.<br>Good rituals.</h2>
            </div>
            <div class="col-lg-6 offset-lg-1 mt-4 mt-lg-0">
                <p class="mb-4" style="font-size: 0.75rem; color: #BDB5B0; letter-spacing: 0.02em;">Be first to know about new launches, thoughtful offers and beauty rituals worth keeping.</p>
                <form class="d-flex align-items-center border-bottom pb-2" style="border-color: rgba(248,246,240,0.3) !important;">
                    <input type="email" class="form-control bg-transparent border-0 px-0 shadow-none" placeholder="Your email address" style="color: #F8F6F0; font-size: 0.85rem;" required>
                    <button type="submit" class="btn p-0 text-decoration-none border-0 bg-transparent" style="color: #F8F6F0;">&rarr;</button>
                </form>
            </div>
        </div>
        
        <!-- Instagram Row (from Mockup 3 "Real Skin. Real Stories.") -->
        <div class="row mt-5 pt-4 fade-up" style="transition-delay: 0.2s;">
            <div class="col-12 mb-4">
                <div class="text-uppercase mb-1" style="font-size: 0.6rem; letter-spacing: 0.15em; color: #8A7E78;">Real People</div>
                <h3 style="font-family: var(--font-serif); font-size: 2.5rem; line-height: 1.1; margin-bottom: 0.5rem; letter-spacing: -0.02em;">Real Skin.<br>Real Stories.</h3>
                <p style="font-size: 0.75rem; color: #BDB5B0;">#RawwishRituals &middot; See how our community uses their favourites.</p>
            </div>
            
            <!-- Instagram Videos -->
            <div class="col-12">
                <div class="row g-3">
                    <div class="col-6 col-lg-3">
                        <iframe src="https://www.instagram.com/p/C8tYSwqK49v/embed" width="100%" height="400" frameborder="0" scrolling="no" allowtransparency="true" style="border-radius: 4px; background: transparent;"></iframe>
                    </div>
                    <div class="col-6 col-lg-3">
                        <iframe src="https://www.instagram.com/p/C76Bul3yW23/embed" width="100%" height="400" frameborder="0" scrolling="no" allowtransparency="true" style="border-radius: 4px; background: transparent;"></iframe>
                    </div>
                    <div class="col-6 col-lg-3">
                        <iframe src="https://www.instagram.com/p/C1uJn1Qh7j3/embed" width="100%" height="400" frameborder="0" scrolling="no" allowtransparency="true" style="border-radius: 4px; background: transparent;"></iframe>
                    </div>
                    <div class="col-6 col-lg-3">
                        <iframe src="https://www.instagram.com/p/C37yEBHBYPN/embed" width="100%" height="400" frameborder="0" scrolling="no" allowtransparency="true" style="border-radius: 4px; background: transparent;"></iframe>
                    </div>
                </div>
            </div>
        </div>
        
    </div>
</section>"""

new_newsletter = """<!-- NEWSLETTER & INSTAGRAM -->
<section class="newsletter-instagram-section py-5" style="background-color: #FAFAFA; color: #231C18;">
    <div class="container py-5">
        <!-- Newsletter Row -->
        <div class="row mb-5 align-items-center fade-up">
            <div class="col-lg-5">
                <div class="text-uppercase mb-3" style="font-size: 0.6rem; letter-spacing: 0.15em; color: #8A7E78;">Join The Rawwish Community</div>
                <h2 style="font-family: var(--font-serif); font-size: clamp(3rem, 5vw, 4.5rem); line-height: 1.05; margin-bottom: 0; letter-spacing: -0.02em;">Good skin.<br>Good rituals.</h2>
            </div>
            <div class="col-lg-6 offset-lg-1 mt-4 mt-lg-0">
                <p class="mb-4" style="font-size: 0.75rem; color: #5A524D; letter-spacing: 0.02em;">Be first to know about new launches, thoughtful offers and beauty rituals worth keeping.</p>
                <form class="d-flex align-items-center border-bottom pb-2" style="border-color: rgba(35,28,24,0.3) !important;">
                    <input type="email" class="form-control bg-transparent border-0 px-0 shadow-none text-dark-newsletter" placeholder="Your email address" style="color: #231C18; font-size: 0.85rem;" required>
                    <button type="submit" class="btn p-0 text-decoration-none border-0 bg-transparent" style="color: #231C18;">&rarr;</button>
                </form>
            </div>
        </div>
        
        <!-- UGC / Real Stories Row -->
        <div class="row mt-5 pt-4 fade-up" style="transition-delay: 0.2s;">
            <div class="col-12 mb-4">
                <div class="text-uppercase mb-1" style="font-size: 0.6rem; letter-spacing: 0.15em; color: #8A7E78;">Real People</div>
                <h3 style="font-family: var(--font-serif); font-size: 2.5rem; line-height: 1.1; margin-bottom: 0.5rem; letter-spacing: -0.02em;">Real Skin.<br>Real Stories.</h3>
                <p style="font-size: 0.75rem; color: #5A524D;">#RawwishRituals &middot; See how our community uses their favourites.</p>
            </div>
            
            <!-- UGC Videos (Webm) -->
            <div class="col-12">
                <div class="row g-3">
                    <div class="col-6 col-lg-3">
                        <video src="/static/main/UGC/1.webm" autoplay loop muted playsinline style="width: 100%; height: 450px; object-fit: cover; border-radius: 4px; background: #EBE5DB;"></video>
                    </div>
                    <div class="col-6 col-lg-3">
                        <video src="/static/main/UGC/2.webm" autoplay loop muted playsinline style="width: 100%; height: 450px; object-fit: cover; border-radius: 4px; background: #EBE5DB;"></video>
                    </div>
                    <div class="col-6 col-lg-3">
                        <video src="/static/main/UGC/3.webm" autoplay loop muted playsinline style="width: 100%; height: 450px; object-fit: cover; border-radius: 4px; background: #EBE5DB;"></video>
                    </div>
                    <div class="col-6 col-lg-3">
                        <video src="/static/main/UGC/4.webm" autoplay loop muted playsinline style="width: 100%; height: 450px; object-fit: cover; border-radius: 4px; background: #EBE5DB;"></video>
                    </div>
                </div>
            </div>
        </div>
        
    </div>
</section>"""

content = content.replace(old_newsletter, new_newsletter)

with open('template/main/index.html', 'w') as f:
    f.write(content)

