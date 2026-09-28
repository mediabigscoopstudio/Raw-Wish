import re

with open('template/main/components/product_card.html', 'r') as f:
    content = f.read()

# Replace the heart button completely
old_button_pattern = r'<button type="button" class="badge-top-right" aria-label="Add to Wishlist".*?</button>'
new_button = """<button type="button" class="badge-top-right" aria-label="Add to Wishlist" 
        onclick="toggleWishlist('{{ product.id }}', this)">
            {% if product.id in global_wishlist_product_ids %}
            <i class="bi bi-heart-fill" style="color: #421035;"></i>
            {% else %}
            <i class="bi bi-heart"></i>
            {% endif %}
        </button>"""

content = re.sub(old_button_pattern, new_button, content, flags=re.DOTALL)

with open('template/main/components/product_card.html', 'w') as f:
    f.write(content)
