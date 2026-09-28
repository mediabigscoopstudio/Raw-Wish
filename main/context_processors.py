from django.conf import settings
from dash.models import Cart, CartItem, Customers, Wishlist, WishlistItem

def cart_processor(request):
    cart_items = []
    cart_total = 0
    cart_count = 0
    
    if not request.session.session_key:
        request.session.create()
    
    cart = None
    if request.user.is_authenticated:
        try:
            customer = Customers.objects.get(user=request.user)
            cart, _ = Cart.objects.get_or_create(customer=customer)
        except Customers.DoesNotExist:
            pass
            
    if not cart:
        session_key = request.session.session_key
        cart, _ = Cart.objects.get_or_create(session_key=session_key)

    if cart:
        cart_items = cart.cart_items.all().select_related('product', 'variant')
        cart_total = sum((item.variant.price if item.variant else 0) * item.quantity for item in cart_items)
        cart_count = sum(item.quantity for item in cart_items)
        
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
        'global_wishlist_product_ids': [item.product_id for item in wishlist_items],
    }

def google_client_id(request):
    return {
        'GOOGLE_CLIENT_ID': getattr(settings, 'GOOGLE_CLIENT_ID', '')
    }

from dash.models import Category, Product
def nav_categories_processor(request):
    categories = Category.objects.prefetch_related('subcategories').all()
    
    # Exclude Accessories to get cosmetics categories only
    cosmetics_products = Product.objects.exclude(category__title__icontains='Accessories').order_by('-id')[:4]
    
    # Get Accessories
    accessories = Product.objects.filter(category__title__icontains='Accessories')[:4]
    
    # Get Featured Product
    featured_product = Product.objects.filter(name__icontains='Hydrating Serum').first()
    
    return {
        'nav_categories': categories,
        'nav_cosmetics_products': cosmetics_products,
        'nav_accessories': accessories,
        'nav_featured_product': featured_product,
    }
