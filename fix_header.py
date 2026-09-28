import re

with open('template/main/components/header.html', 'r') as f:
    content = f.read()

# 1. Remove the misplaced mobile wishlist from the desktop section
mobile_wishlist_block = """
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
content = content.replace(mobile_wishlist_block, "")

# 2. Insert the mobile wishlist correctly in the mobile section before the Cart Button
mobile_wishlist_clean = """
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

                <!-- Cart Button -->"""

# We need to target the second "<!-- Cart Button -->"
# The desktop one is now just followed by <!-- Cart Button -->
# Let's split by "<!-- Cart Button -->"
parts = content.split("<!-- Cart Button -->")
# parts[0] is everything before desktop cart
# parts[1] is everything between desktop cart and mobile cart
# parts[2] is everything after mobile cart
if len(parts) >= 3:
    # Reassemble with the mobile wishlist inserted in the second slot
    content = parts[0] + "<!-- Cart Button -->" + parts[1] + mobile_wishlist_clean + parts[2]

# 3. Update the mobile logo
content = content.replace(
    '<img src="/static/main/logos/vector.webp" alt="Rawwish Icon" style="height: 35px; object-fit: contain;">',
    '<img src="/static/main/logos/Logo.webp" alt="Rawwish Logo" style="height: 40px; object-fit: contain;">'
)

with open('template/main/components/header.html', 'w') as f:
    f.write(content)
