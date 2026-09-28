import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rawwish.settings")
django.setup()

from dash.models import Category, SubCategory, Product, Variant, ProductImage, Offer, SupportQuery, Customers, Order, ProductAttribute, ProductAttributeValue
from django.contrib.auth.models import User

print("Wiping database...")

# Commerce
Order.objects.all().delete()
Customers.objects.all().delete()

# Wait, if we delete customers, should we delete non-staff users? 
# Let's clean non-staff users so they don't linger.
User.objects.filter(is_staff=False, is_superuser=False).delete()

# Support
SupportQuery.objects.all().delete()

# Catalogue
ProductImage.objects.all().delete()
Variant.objects.all().delete()
ProductAttributeValue.objects.all().delete()
ProductAttribute.objects.all().delete()
Product.objects.all().delete()
SubCategory.objects.all().delete()
Category.objects.all().delete()

# Marketing
Offer.objects.all().delete()

print("All requested data has been completely deleted!")
