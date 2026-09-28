from django.contrib import admin
from django.urls import path
from django.contrib.sitemaps.views import sitemap
from main.sitemaps import ProductSitemap, StaticViewSitemap
from django.views.generic import TemplateView
from main import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


sitemaps = {
    'static': StaticViewSitemap,
    'products': ProductSitemap,
}

urlpatterns = [
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('llms.txt', TemplateView.as_view(template_name='llms.txt', content_type='text/plain')),

    path('my-orders/', views.my_orders, name='my_orders'),
    path('api/search/', views.search_products_api, name='search_products_api'),
    path('my-orders/<str:display_id>/', views.my_order_detail, name='my_order_detail'),
    path('support/', views.support_list, name='customer_support'),
    path('support/new/', views.support_create, name='support_create'),
    path('support/<str:support_id>/', views.support_chat, name='support_chat'),
    path('api/support/<str:support_id>/message/', views.api_support_message, name='api_support_message'),

    path('auth/google-login/', views.google_login, name='google_login'),
    path('logout/', views.custom_logout, name='logout'),
    path('subscribe-newsletter/', views.subscribe_newsletter, name='subscribe_newsletter'),

    path("", views.index, name='index'),
    path("about/", views.about, name='about'),
    path("ingredients/", views.ingredients, name='ingredients'),
    path("learn", views.learn, name='learn'),
    
    # CMS / Content Routes
    path("content/", views.content, name='content'),
    # Shop Routes
    path("shop/", views.shop, name='shop'),
    path("shop/category/<slug:category_slug>/", views.shop, name='shop_category'),
    path("shop/add-to-cart/", views.add_to_cart, name='add_to_cart'),
    path('checkout/', views.checkout, name='checkout'),
        path('verify_payment/', views.verify_payment, name='verify_payment'),
    

    # Wishlist APIs
    path('api/wishlist/toggle/', views.toggle_wishlist, name='toggle_wishlist'),
    path('api/wishlist/remove/', views.remove_wishlist, name='remove_wishlist'),

    # Fast Checkout APIs
    path('api/fc/state/', views.fc_get_state, name='fc_get_state'),
    path('api/fc/cart/update/', views.fc_update_cart, name='fc_update_cart'),
    path('api/fc/coupon/apply/', views.fc_apply_coupon, name='fc_apply_coupon'),
    path('api/fc/payment/init/', views.fc_init_payment, name='fc_init_payment'),
    path('api/fc/payment/verify/', views.fc_verify_payment, name='fc_verify_payment'),


    path("<slug:category_slug>/<slug:subcategory_slug>/<slug:product_slug>/", views.product_detail, name='product_detail'),
    
    # Must come after exact matches to avoid catching them
    path("<slug:category_slug>/", views.content, name='category_detail'),
    path("<slug:category_slug>/<slug:article_slug>/", views.article_detail, name='article_detail'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
