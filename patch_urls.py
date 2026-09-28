import re

with open('main/urls.py', 'r') as f:
    content = f.read()

wishlist_urls = """
    # Wishlist APIs
    path('api/wishlist/toggle/', views.toggle_wishlist, name='toggle_wishlist'),
    path('api/wishlist/remove/', views.remove_wishlist, name='remove_wishlist'),
"""

content = content.replace("    # Fast Checkout APIs", wishlist_urls + "\n    # Fast Checkout APIs")

with open('main/urls.py', 'w') as f:
    f.write(content)
