with open('template/main/index.html', 'r') as f:
    content = f.read()

old_loop = """            {% for product in featured_products|slice:":4" %}
            <div class="col-6 col-lg-3 fade-up">
                <div class="card product-card h-100 bg-transparent">
                    <a href="{% url 'product_detail' product.category.slug product.sub_category.slug product.slug %}" class="text-decoration-none">
                        {% if product.product_images.first %}
                        <img src="{{ product.product_images.first.image.url }}" class="card-img-top" alt="{{ product.name }}" loading="lazy">
                        {% else %}
                        <img src="/static/main/images/product_1.webp" class="card-img-top" alt="{{ product.name }}" loading="lazy">
                        {% endif %}
                        <div class="card-body px-0">
                            <div class="text-uppercase text-muted-rw mb-1" style="font-size: 0.75rem; letter-spacing: 0.05em;">{{ product.category.title }}</div>
                            <h3 class="product-card-title">{{ product.name }}</h3>
                            <div class="product-card-price">
                                {% if product.product_variant.first %}
                                    ₹{{ product.product_variant.first.price|floatformat:0 }}
                                {% else %}
                                    View Options
                                {% endif %}
                            </div>
                        </div>
                    </a>
                </div>
            </div>
            {% empty %}"""

new_loop = """            {% for product in featured_products|slice:":4" %}
            <div class="col-6 col-lg-3 fade-up">
                {% include 'main/components/product_card.html' with product=product %}
            </div>
            {% empty %}"""

content = content.replace(old_loop, new_loop)

with open('template/main/index.html', 'w') as f:
    f.write(content)
