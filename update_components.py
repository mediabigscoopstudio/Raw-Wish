import re

# Update product_card.html
with open('template/main/components/product_card.html', 'r') as f:
    card_html = f.read()

# 1. Remove Reviews
card_html = re.sub(r'<div class="rawwish-reviews">.*?</div>', '', card_html, flags=re.DOTALL)

# 2. Remove Variant Label
card_html = re.sub(r'<div class="variant-label">.*?</div>', '', card_html, flags=re.DOTALL)

# 3. Add onclick to wishlist button
card_html = card_html.replace(
    '<button type="button" class="badge-top-right" aria-label="Add to Wishlist">',
    """<button type="button" class="badge-top-right" aria-label="Add to Wishlist" 
        onclick="toggleWishlist('{{ product.id }}', '{{ product.name|escapejs }}', '{% if product.product_images.first %}{{ product.product_images.first.image.url }}{% else %}/static/main/images/product_1.webp{% endif %}', '{% url 'product_detail' product.category.slug product.sub_category.slug|default:'all' product.slug %}')"
        data-wishlist-btn="{{ product.id }}">"""
)

# 4. Make wishlist button heart dynamic
card_html = card_html.replace('<i class="bi bi-heart"></i>', '<i class="bi bi-heart" id="wishlist-icon-{{ product.id }}"></i>')

with open('template/main/components/product_card.html', 'w') as f:
    f.write(card_html)


# Update header.html
with open('template/main/components/header.html', 'r') as f:
    header_html = f.read()

# Change cart-badge color to #421035
header_html = header_html.replace(
    'background-color:var(--rawwish-plantation,#2D5A3D);',
    'background-color:#421035;'
)

# Add Wishlist to desktop nav
wishlist_desktop = """
                <!-- Wishlist Dropdown -->
                <div class="dropdown me-3">
                    <a href="#" class="header-icon position-relative" data-bs-toggle="dropdown" aria-expanded="false" id="wishlistDropdownDesktop">
                        <i class="bi bi-heart"></i>
                        <span class="cart-badge" id="wishlist-badge-desktop" style="display: none;">0</span>
                    </a>
                    <ul class="dropdown-menu dropdown-menu-end p-3 shadow" style="width: 300px; max-height: 400px; overflow-y: auto;" id="wishlist-menu-desktop">
                        <li class="text-center text-muted">Your wishlist is empty</li>
                    </ul>
                </div>
"""

# Insert before Cart button in desktop
header_html = re.sub(r'(<!-- Cart Button -->)', wishlist_desktop + r'\1', header_html, count=1)

# Add Wishlist to mobile nav
wishlist_mobile = """
                <!-- Wishlist Mobile -->
                <div class="dropdown me-3">
                    <a href="#" class="header-icon position-relative" data-bs-toggle="dropdown" aria-expanded="false" id="wishlistDropdownMobile">
                        <i class="bi bi-heart"></i>
                        <span class="cart-badge" id="wishlist-badge-mobile" style="display: none;">0</span>
                    </a>
                    <ul class="dropdown-menu dropdown-menu-end p-3 shadow" style="width: 250px; max-height: 300px; overflow-y: auto;" id="wishlist-menu-mobile">
                        <li class="text-center text-muted">Your wishlist is empty</li>
                    </ul>
                </div>
"""
header_html = re.sub(r'(<!-- Cart Button -->)', wishlist_mobile + r'\1', header_html, count=1) # The second occurrence is in mobile

with open('template/main/components/header.html', 'w') as f:
    f.write(header_html)
