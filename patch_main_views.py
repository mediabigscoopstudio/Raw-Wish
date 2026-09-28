import re

with open('main/views.py', 'r') as f:
    content = f.read()

# Replace the specific block of code for the index view
old_block = """    # 2. Bestseller Products (Eagerly fetch variants to prevent N+1 queries)
    bestseller_names = [
        'Raw Wish Vitamin C Face Wash',
        'Raw Wish Hydrating Serum',
        'Raw Wish South Indian Cosmetics Filter',
        'Raw Wish Matte Lipstick'
    ]
    bestseller_products = []
    for name in bestseller_names:
        prod = Product.objects.prefetch_related('product_variant').filter(name__icontains=name.replace('Raw Wish ', '')).first()
        if prod:
            bestseller_products.append(prod)
    
    context = {
        'categories': categories,
        'bestseller_products': bestseller_products,"""

new_block = """    # 2. Featured Products
    featured_products = Product.objects.prefetch_related('variants', 'images').all()[:4]
    
    context = {
        'categories': categories,
        'featured_products': featured_products,"""

content = content.replace(old_block, new_block)

with open('main/views.py', 'w') as f:
    f.write(content)
