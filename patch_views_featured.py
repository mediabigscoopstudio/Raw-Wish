with open('main/views.py', 'r') as f:
    content = f.read()

old_block = """    # 2. Featured Products
    featured_products = Product.objects.prefetch_related('product_variant', 'product_images').all()[:4]"""

new_block = """    # 2. Featured Products
    target_product_names = [
        'Hydrating Lip Tint',
        'Velvet Matte Lip Colour',
        'Shea Butter Body Lotion',
        'Niacinamide + Zinc Balancing Serum'
    ]
    featured_products = list(Product.objects.prefetch_related('product_variant', 'product_images').filter(name__in=target_product_names))
    # Order them to match the requested sequence if needed, but simple list is fine."""

content = content.replace(old_block, new_block)

with open('main/views.py', 'w') as f:
    f.write(content)
