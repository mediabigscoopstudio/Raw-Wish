import re
import os

# 1. Create product_card.html
card_html = """
<div class="rawwish-card h-100">
    <!-- Image & Badges -->
    <div class="rawwish-card-img-wrap">
        <a href="{% url 'product_detail' product.category.slug product.sub_category.slug|default:'all' product.slug %}" style="display:block; width:100%; height:100%;">
            {% if product.product_images.first %}
                <img src="{{ product.product_images.first.image.url }}" alt="{{ product.name }}" loading="lazy">
            {% elif product.thumbnail %}
                <img src="{{ product.thumbnail.url }}" alt="{{ product.name }}" loading="lazy">
            {% else %}
                <img src="/static/main/images/product_1.webp" alt="{{ product.name }}" loading="lazy" style="object-fit: cover;">
            {% endif %}
        </a>
        
        {% if product.category %}
        <a href="{% url 'shop_category' product.category.slug %}" class="badge-top-left" style="text-decoration:none; transition:transform 0.2s;">
            <i class="bi bi-tag-fill" style="color:var(--rw-plum);"></i> {{ product.category.title }}
        </a>
        {% endif %}
        
        <button type="button" class="badge-top-right" aria-label="Add to Wishlist">
            <i class="bi bi-heart"></i>
        </button>
    </div>

    <!-- Card Body -->
    <div class="rawwish-card-body">
        <a href="{% url 'product_detail' product.category.slug product.sub_category.slug|default:'all' product.slug %}" class="rawwish-title-link">
            <h3 class="rawwish-title">{{ product.name }}</h3>
        </a>
        
        <div class="rawwish-reviews">
            <i class="bi bi-star-fill"></i> <strong>4.8</strong> <span style="color:var(--rw-muted);">(320 reviews)</span>
        </div>

        <!-- Form / Add to Cart Section -->
        <form action="{% url 'add_to_cart' %}" method="POST" class="add-to-cart-form" style="margin-top:auto; display:flex; flex-direction:column;">
            {% csrf_token %}
            <input type="hidden" name="product_id" value="{{ product.id }}">
            
            {% if product.product_variant.all %}
                <div class="variant-label">Select Option</div>
                <div class="variant-grid">
                    {% for v in product.product_variant.all %}
                    <div class="v-box">
                        <input type="radio" name="variant_id" id="v_{{ product.id }}_{{ v.id }}" value="{{ v.id }}" 
                               {% if forloop.first %}checked{% endif %} 
                               onchange="document.getElementById('price_main_{{ product.id }}').innerText = '₹{{ v.price|floatformat:0 }}';">
                        <label class="v-label-pill" for="v_{{ product.id }}_{{ v.id }}">
                            {{ v.name }}
                        </label>
                    </div>
                    {% endfor %}
                </div>
            {% endif %}
            
            <div class="price-qty-row">
                <div class="price-block">
                    <div class="price-main" id="price_main_{{ product.id }}">
                        {% if product.product_variant.first %}₹{{ product.product_variant.first.price|floatformat:0 }}{% else %}N/A{% endif %}
                    </div>
                    <div class="price-tax">Inclusive of all taxes</div>
                </div>
                
                <div class="qty-selector">
                    <button type="button" class="qty-btn" onclick="let inp=document.getElementById('qty_{{ product.id }}'); inp.value=Math.max(1, parseInt(inp.value)-1);">&minus;</button>
                    <input type="number" id="qty_{{ product.id }}" name="quantity" value="1" min="1" class="qty-input" readonly>
                    <button type="button" class="qty-btn" onclick="let inp=document.getElementById('qty_{{ product.id }}'); inp.value=parseInt(inp.value)+1;">&plus;</button>
                </div>
            </div>

            <button type="submit" class="btn-add-cart-dark" {% if not product.product_variant.all %}disabled{% endif %}>
                <i class="bi bi-bag"></i> Add to Cart
            </button>
        </form>
    </div>
</div>
"""
os.makedirs('template/main/components', exist_ok=True)
with open('template/main/components/product_card.html', 'w') as f:
    f.write(card_html)
