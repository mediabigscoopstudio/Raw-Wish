with open('template/main/components/footer.html', 'r') as f:
    content = f.read()

# Let's completely replace the footer part while keeping the Pinecode Studio Modal at the end.
# We'll split the content at "<!-- Pinecode Studio Modal -->"
parts = content.split('<!-- Pinecode Studio Modal -->')

new_footer = """<footer class="footer pt-5">
    <div class="container py-4">
        <div class="row g-5">
            <div class="col-lg-4 mb-4 mb-lg-0">
                <img src="/static/main/logos/LogoMain.webp" alt="Rawwish" height="45" class="mb-4" style="filter: brightness(0) invert(1);">
                <p class="text-white-50 small mb-4" style="max-width: 300px; line-height: 1.6;">
                    Thoughtfully crafted beauty essentials with clean ingredients, real intention and a deeper respect for you and the planet.
                </p>
                <div class="d-flex gap-3">
                    <a href="#" class="text-white-50 hover-white fs-5"><i class="bi bi-instagram"></i></a>
                    <a href="#" class="text-white-50 hover-white fs-5"><i class="bi bi-facebook"></i></a>
                    <a href="#" class="text-white-50 hover-white fs-5"><i class="bi bi-twitter-x"></i></a>
                </div>
            </div>
            
            <div class="col-6 col-lg-2">
                <h6 class="text-uppercase fw-bold mb-4 text-white" style="letter-spacing: 0.1em; font-size: 0.85rem;">Shop</h6>
                <ul class="list-unstyled d-flex flex-column gap-3 small">
                    <li><a href="/shop/?category=skincare">Skincare</a></li>
                    <li><a href="/shop/?category=body-care">Body Care</a></li>
                    <li><a href="/shop/?category=lip-care">Lip Care</a></li>
                    <li><a href="/shop/?category=haircare">Haircare</a></li>
                    <li><a href="/shop/?category=gift-sets">Gift Sets</a></li>
                </ul>
            </div>
            
            <div class="col-6 col-lg-2">
                <h6 class="text-uppercase fw-bold mb-4 text-white" style="letter-spacing: 0.1em; font-size: 0.85rem;">About</h6>
                <ul class="list-unstyled d-flex flex-column gap-3 small">
                    <li><a href="/about">Our Story</a></li>
                    <li><a href="/about#ingredients">Ingredients</a></li>
                    <li><a href="/sustainability">Sustainability</a></li>
                    <li><a href="/journal">Journal</a></li>
                </ul>
            </div>
            
            <div class="col-6 col-lg-2">
                <h6 class="text-uppercase fw-bold mb-4 text-white" style="letter-spacing: 0.1em; font-size: 0.85rem;">Support</h6>
                <ul class="list-unstyled d-flex flex-column gap-3 small">
                    <li><a href="/shipping">Shipping</a></li>
                    <li><a href="/returns">Returns</a></li>
                    <li><a href="/faq">FAQs</a></li>
                    <li><a href="/track">Track Order</a></li>
                    <li><a href="/support">Help Center</a></li>
                </ul>
            </div>
        </div>
        
        <hr class="border-secondary my-5" style="opacity: 0.2;">
        
        <div class="d-flex flex-column flex-md-row justify-content-between align-items-center small text-white-50">
            <p class="mb-3 mb-md-0">&copy; 2026 Rawwish. All rights reserved.</p>
            <div class="d-flex gap-4">
                <a href="/privacy">Privacy Policy</a>
                <a href="/terms">Terms & Conditions</a>
            </div>
        </div>

        <div class="mt-4 text-center pb-2">
            <span class="text-white-50 small">Designed & Developed by </span>
            <a href="#" class="fw-bold text-decoration-none small" style="color: var(--rw-dusty-rose);" data-bs-toggle="modal" data-bs-target="#pinecodeModal">Pinecode Studio LLP</a>
        </div>
    </div>
</footer>

<!-- Pinecode Studio Modal -->"""

with open('template/main/components/footer.html', 'w') as f:
    f.write(new_footer + parts[1] if len(parts) > 1 else new_footer)
