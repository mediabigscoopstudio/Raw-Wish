with open('main/context_processors.py', 'r') as f:
    content = f.read()

content = content.replace("'global_wishlist_count': wishlist_count,",
                          "'global_wishlist_count': wishlist_count,\n        'global_wishlist_product_ids': [item.product_id for item in wishlist_items],")

with open('main/context_processors.py', 'w') as f:
    f.write(content)
