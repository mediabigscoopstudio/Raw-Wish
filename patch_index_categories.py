with open('template/main/index.html', 'r') as f:
    content = f.read()

# Replace the entire categories row
old_categories_row = """        <div class="row g-4">
            <!-- Fetch Categories from Backend if possible, or use static links mirroring the db -->
            <div class="col-6 col-md-3 fade-up">
                <a href="/shop/?category=skincare" class="category-card">
                    <img src="/static/main/images/category-skincare.webp" alt="Skincare" loading="lazy">
                    <div class="category-overlay">
                        <h3 class="category-title">Skincare</h3>
                        <div class="category-subtitle">Explore <i class="bi bi-arrow-right"></i></div>
                    </div>
                </a>
            </div>
            <div class="col-6 col-md-3 fade-up" style="transition-delay: 0.1s;">
                <a href="/shop/?category=haircare" class="category-card">
                    <img src="/static/main/images/category-haircare.webp" alt="Haircare" loading="lazy">
                    <div class="category-overlay">
                        <h3 class="category-title">Haircare</h3>
                        <div class="category-subtitle">Explore <i class="bi bi-arrow-right"></i></div>
                    </div>
                </a>
            </div>
            <div class="col-6 col-md-3 fade-up" style="transition-delay: 0.2s;">
                <a href="/shop/?category=makeup" class="category-card">
                    <img src="/static/main/images/category-makeup.webp" alt="Makeup" loading="lazy">
                    <div class="category-overlay">
                        <h3 class="category-title">Makeup</h3>
                        <div class="category-subtitle">Explore <i class="bi bi-arrow-right"></i></div>
                    </div>
                </a>
            </div>
            <div class="col-6 col-md-3 fade-up" style="transition-delay: 0.3s;">
                <a href="/shop/?category=body-care" class="category-card">
                    <img src="/static/main/images/category-body.webp" alt="Body Care" loading="lazy">
                    <div class="category-overlay">
                        <h3 class="category-title">Body Care</h3>
                        <div class="category-subtitle">Explore <i class="bi bi-arrow-right"></i></div>
                    </div>
                </a>
            </div>
        </div>"""

new_categories_row = """        <div class="row g-4">
            {% for cat in categories|slice:":4" %}
            <div class="col-6 col-md-3 fade-up" style="transition-delay: 0.{{ forloop.counter0 }}s;">
                <a href="{% url 'shop_category' cat.slug %}" class="category-card">
                    {% if cat.image %}
                    <img src="{{ cat.image.url }}" alt="{{ cat.title }}" loading="lazy">
                    {% else %}
                    <img src="/static/main/images/placeholder.webp" alt="{{ cat.title }}" loading="lazy">
                    {% endif %}
                    <div class="category-overlay">
                        <h3 class="category-title">{{ cat.title }}</h3>
                        <div class="category-subtitle">Explore <i class="bi bi-arrow-right"></i></div>
                    </div>
                </a>
            </div>
            {% empty %}
            <p>No categories found.</p>
            {% endfor %}
        </div>"""

content = content.replace(old_categories_row, new_categories_row)

with open('template/main/index.html', 'w') as f:
    f.write(content)
