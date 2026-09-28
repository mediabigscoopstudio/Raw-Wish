import re

with open('main/context_processors.py', 'r') as f:
    content = f.read()

# Add Wishlist, WishlistItem imports
content = content.replace("from dash.models import Cart, CartItem, Customers", "from dash.models import Cart, CartItem, Customers, Wishlist, WishlistItem")

# Add wishlist logic inside cart_processor
wishlist_logic = """
    wishlist_items = []
    wishlist_count = 0
    
    wishlist = None
    if request.user.is_authenticated:
        try:
            customer = Customers.objects.get(user=request.user)
            wishlist, _ = Wishlist.objects.get_or_create(customer=customer)
        except Customers.DoesNotExist:
            pass
            
    if not wishlist:
        wishlist, _ = Wishlist.objects.get_or_create(session_key=request.session.session_key)

    if wishlist:
        wishlist_items = wishlist.wishlist_items.all().select_related('product', 'variant')
        wishlist_count = wishlist_items.count()

    return {
        'global_cart_items': cart_items,
        'global_cart_total': cart_total,
        'global_cart_count': cart_count,
        'global_wishlist_items': wishlist_items,
        'global_wishlist_count': wishlist_count,
    }
"""

content = re.sub(r"return \{\s*'global_cart_items': cart_items,.*?\}", wishlist_logic.strip(), content, flags=re.DOTALL)

with open('main/context_processors.py', 'w') as f:
    f.write(content)
