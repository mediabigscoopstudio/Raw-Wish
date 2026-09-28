import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rawwish.settings")
django.setup()

from dash.models import Category, SubCategory, Product, Offer, SupportQuery, Customers, Order

print(f"Categories: {Category.objects.count()}")
print(f"Products: {Product.objects.count()}")
print(f"Orders: {Order.objects.count()}")
print(f"Customers: {Customers.objects.count()}")
print(f"Support Queries: {SupportQuery.objects.count()}")
print(f"Offers: {Offer.objects.count()}")
