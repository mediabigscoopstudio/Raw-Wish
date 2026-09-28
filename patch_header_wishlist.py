import re

with open('template/main/components/header.html', 'r') as f:
    content = f.read()

# Replace the HTML for the Wishlist Dropdown in both desktop and mobile
desktop_wishlist_html = """
                <!-- Wishlist Dropdown -->
                <div class="dropdown me-3">
                    <a href="#" class="header-icon position-relative" data-bs-toggle="dropdown" aria-expanded="false" id="wishlistDropdownDesktop">
                        <i class="bi bi-heart"></i>
                        <span class="cart-badge wishlist-badge-counter" style="display: {% if global_wishlist_count > 0 %}flex{% else %}none{% endif %};">{{ global_wishlist_count }}</span>
                    </a>
                    <ul class="dropdown-menu dropdown-menu-end p-3 shadow wishlist-menu-dropdown" style="width: 300px; max-height: 400px; overflow-y: auto;">
                        {% if global_wishlist_count == 0 %}
                        <li class="text-center text-muted" style="font-size: 0.85rem; padding: 10px;">Your wishlist is empty</li>
                        {% else %}
                            {% for item in global_wishlist_items %}
                            <li class="mb-3 wishlist-item-{{ item.id }}">
                                <div class="d-flex align-items-center position-relative">
                                    <img src="{% if item.product.product_images.first %}{{ item.product.product_images.first.image.url }}{% else %}/static/main/images/product_1.webp{% endif %}" alt="{{ item.product.name }}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 4px; margin-right: 10px;">
                                    <a href="{% url 'product_detail' item.product.category.slug item.product.sub_category.slug|default:'all' item.product.slug %}" class="text-decoration-none text-dark" style="font-size: 0.85rem; font-weight: 600; line-height: 1.2; flex-grow: 1;">{{ item.product.name }}</a>
                                    <button class="btn btn-sm text-danger p-0 ms-2" onclick="removeWishlistItem('{{ item.id }}', event)"><i class="bi bi-trash"></i></button>
                                </div>
                            </li>
                            {% endfor %}
                        {% endif %}
                    </ul>
                </div>
"""

mobile_wishlist_html = desktop_wishlist_html.replace('wishlistDropdownDesktop', 'wishlistDropdownMobile')
mobile_wishlist_html = mobile_wishlist_html.replace('<!-- Wishlist Dropdown -->', '<!-- Wishlist Mobile -->')
mobile_wishlist_html = mobile_wishlist_html.replace('width: 300px;', 'width: 250px;')

# We need to replace the old blocks carefully.
content = re.sub(r'<!-- Wishlist Dropdown -->.*?</ul>\s*</div>', desktop_wishlist_html.strip(), content, flags=re.DOTALL)
content = re.sub(r'<!-- Wishlist Mobile -->.*?</ul>\s*</div>', mobile_wishlist_html.strip(), content, flags=re.DOTALL)

# Replace the script block entirely
new_script = """
<script>
    // Server-synced Wishlist Logic
    
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    const csrftoken = getCookie('csrftoken');

    function toggleWishlist(productId, btnElement) {
        fetch('/api/wishlist/toggle/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({ product_id: productId })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // We'll just reload the page for now to keep the UI perfectly synced with the backend 
                // since the dropdown HTML is rendered by Django. A full SPA approach would rebuild the HTML here.
                window.location.reload();
            } else {
                console.error(data.error);
            }
        });
    }

    function removeWishlistItem(itemId, event) {
        if(event) { event.preventDefault(); event.stopPropagation(); }
        fetch('/api/wishlist/remove/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({ item_id: itemId })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                window.location.reload();
            }
        });
    }
</script>
"""

content = re.sub(r'<script>\s*// Wishlist Logic using localStorage.*?</script>', new_script.strip(), content, flags=re.DOTALL)

with open('template/main/components/header.html', 'w') as f:
    f.write(content)
