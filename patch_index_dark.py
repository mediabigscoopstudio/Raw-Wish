with open('template/main/index.html', 'r') as f:
    content = f.read()

start_idx = content.find('<!-- EDITORIAL BRAND STORY -->')
end_idx = content.find("{% endblock 'body' %}")

if start_idx != -1 and end_idx != -1:
    new_html = """<!-- EDITORIAL BRAND STORY -->
<section class="more-than-beauty" style="background-color: #2F1A1B; overflow: hidden;">
    <div class="row g-0">
        <div class="col-lg-5 d-flex align-items-center" style="padding: 10%;">
            <div class="fade-up" style="color: #F8F6F0;">
                <div class="text-uppercase mb-4" style="font-size: 0.6rem; letter-spacing: 0.15em; color: #B59A98;">Our Philosophy</div>
                <h2 class="mb-4" style="font-family: var(--font-serif); font-size: clamp(3rem, 5vw, 5.5rem); line-height: 1.05; letter-spacing: -0.02em;">More Than<br>Beauty.</h2>
                <p class="mb-5" style="font-size: 0.85rem; line-height: 1.8; max-width: 400px; color: #E0D3D1;">
                    Self-care is a form of power. Rawwish products are made with real ingredients, real intention and a deep respect for you and the planet.
                </p>
                <a href="/about" class="text-uppercase text-decoration-none" style="color: #F8F6F0; font-size: 0.65rem; letter-spacing: 0.15em; border-bottom: 1px solid #F8F6F0; padding-bottom: 4px;">Our Story &rarr;</a>
            </div>
        </div>
        <div class="col-lg-7">
            <img src="/static/main/images/product_1.webp" alt="More Than Beauty" style="width: 100%; height: 100%; object-fit: cover; min-height: 500px;">
        </div>
    </div>
</section>

<!-- INGREDIENTS -->
<section class="ingredients-section py-5" style="background-color: #4A2B2D; overflow-x: hidden;">
    <div class="container-fluid py-5 px-lg-5">
        <div class="row align-items-center">
            <!-- Left Text -->
            <div class="col-lg-3 pe-lg-5 mb-5 mb-lg-0 fade-up">
                <div class="text-uppercase mb-4" style="font-size: 0.6rem; letter-spacing: 0.15em; color: #D1B8B6;">Nature's Finest</div>
                <h2 class="mb-4" style="font-family: var(--font-serif); font-size: clamp(3rem, 5vw, 4.5rem); line-height: 1.05; color: #F8F6F0; letter-spacing: -0.02em;">Ingredients<br>That Care.</h2>
                <p class="mb-5" style="font-size: 0.85rem; line-height: 1.8; color: #E0D3D1;">
                    Thoughtfully chosen, high-quality ingredients that are gentle, effective and good for your skin &mdash; and the planet.
                </p>
                <a href="/ingredients" class="text-uppercase text-decoration-none" style="color: #F8F6F0; font-size: 0.65rem; letter-spacing: 0.15em; border-bottom: 1px solid #F8F6F0; padding-bottom: 4px;">Explore Ingredients &rarr;</a>
            </div>
            
            <!-- Right Grid -->
            <div class="col-lg-9 fade-up" style="transition-delay: 0.2s;">
                <div class="row row-cols-2 row-cols-md-4 g-3">
                    
                    <div class="col">
                        <img src="/static/main/images/product_1.webp" alt="Coffee" style="width: 100%; height: 180px; object-fit: cover; margin-bottom: 0;">
                        <div style="background-color: #F8F6F0; padding: 12px 15px;">
                            <h4 class="mb-1" style="font-family: var(--font-serif); font-size: 1rem; color: #231C18;">Coffee</h4>
                            <p class="mb-0" style="font-size: 0.6rem; color: #5A524D;">Energises & revitalises</p>
                        </div>
                    </div>
                    
                    <div class="col">
                        <img src="/static/main/images/product_1.webp" alt="Shea Butter" style="width: 100%; height: 180px; object-fit: cover; margin-bottom: 0;">
                        <div style="background-color: #F8F6F0; padding: 12px 15px;">
                            <h4 class="mb-1" style="font-family: var(--font-serif); font-size: 1rem; color: #231C18;">Shea Butter</h4>
                            <p class="mb-0" style="font-size: 0.6rem; color: #5A524D;">Nourishes & repairs</p>
                        </div>
                    </div>

                    <div class="col">
                        <img src="/static/main/images/product_1.webp" alt="Aloe Vera" style="width: 100%; height: 180px; object-fit: cover; margin-bottom: 0;">
                        <div style="background-color: #F8F6F0; padding: 12px 15px;">
                            <h4 class="mb-1" style="font-family: var(--font-serif); font-size: 1rem; color: #231C18;">Aloe Vera</h4>
                            <p class="mb-0" style="font-size: 0.6rem; color: #5A524D;">Calms & heals</p>
                        </div>
                    </div>

                    <div class="col">
                        <img src="/static/main/images/product_1.webp" alt="Turmeric" style="width: 100%; height: 180px; object-fit: cover; margin-bottom: 0;">
                        <div style="background-color: #F8F6F0; padding: 12px 15px;">
                            <h4 class="mb-1" style="font-family: var(--font-serif); font-size: 1rem; color: #231C18;">Turmeric</h4>
                            <p class="mb-0" style="font-size: 0.6rem; color: #5A524D;">Brightens & protects</p>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>
</section>

<!-- NEWSLETTER & INSTAGRAM -->
<section class="newsletter-instagram-section py-5" style="background-color: #1F1112; color: #F8F6F0;">
    <div class="container py-5">
        <!-- Newsletter Row -->
        <div class="row mb-5 align-items-center fade-up">
            <div class="col-lg-5">
                <div class="text-uppercase mb-3" style="font-size: 0.6rem; letter-spacing: 0.15em; color: #9A7B7A;">Join The Rawwish Community</div>
                <h2 style="font-family: var(--font-serif); font-size: clamp(3rem, 5vw, 4.5rem); line-height: 1.05; margin-bottom: 0; letter-spacing: -0.02em;">Good skin.<br>Good rituals.</h2>
            </div>
            <div class="col-lg-6 offset-lg-1 mt-4 mt-lg-0">
                <p class="mb-4" style="font-size: 0.75rem; color: #D1B8B6; letter-spacing: 0.02em;">Be first to know about new launches, thoughtful offers and beauty rituals worth keeping.</p>
                <form class="d-flex align-items-center border-bottom pb-2" style="border-color: rgba(248,246,240,0.3) !important;">
                    <input type="email" class="form-control bg-transparent border-0 px-0 shadow-none text-light" placeholder="Your email address" style="color: #F8F6F0; font-size: 0.85rem;" required>
                    <button type="submit" class="btn p-0 text-decoration-none border-0 bg-transparent" style="color: #F8F6F0;">&rarr;</button>
                </form>
            </div>
        </div>
        
        <!-- UGC / Real Stories Row -->
        <div class="row mt-5 pt-4 fade-up" style="transition-delay: 0.2s;">
            <div class="col-12 mb-4">
                <div class="text-uppercase mb-1" style="font-size: 0.6rem; letter-spacing: 0.15em; color: #9A7B7A;">Real People</div>
                <h3 style="font-family: var(--font-serif); font-size: 2.5rem; line-height: 1.1; margin-bottom: 0.5rem; letter-spacing: -0.02em;">Real Skin.<br>Real Stories.</h3>
                <p style="font-size: 0.75rem; color: #D1B8B6;">#RawwishRituals &middot; See how our community uses their favourites.</p>
            </div>
            
            <!-- UGC Videos (Webm) -->
            <div class="col-12">
                <div class="row g-3">
                    <div class="col-6 col-lg-3">
                        <video src="/static/main/UGC/1.webm" autoplay loop muted playsinline style="width: 100%; height: 450px; object-fit: cover; border-radius: 4px; background: #2B1618;"></video>
                    </div>
                    <div class="col-6 col-lg-3">
                        <video src="/static/main/UGC/2.webm" autoplay loop muted playsinline style="width: 100%; height: 450px; object-fit: cover; border-radius: 4px; background: #2B1618;"></video>
                    </div>
                    <div class="col-6 col-lg-3">
                        <video src="/static/main/UGC/3.webm" autoplay loop muted playsinline style="width: 100%; height: 450px; object-fit: cover; border-radius: 4px; background: #2B1618;"></video>
                    </div>
                    <div class="col-6 col-lg-3">
                        <video src="/static/main/UGC/4.webm" autoplay loop muted playsinline style="width: 100%; height: 450px; object-fit: cover; border-radius: 4px; background: #2B1618;"></video>
                    </div>
                </div>
            </div>
        </div>
        
    </div>
</section>
"""

    new_content = content[:start_idx] + new_html + content[end_idx:]
    with open('template/main/index.html', 'w') as f:
        f.write(new_content)

