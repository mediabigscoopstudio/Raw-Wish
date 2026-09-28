import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rawwish.settings")
django.setup()

from dash.models import Category, SubCategory
from django.utils.text import slugify

print("Deleting old categories...")
Category.objects.all().delete()
SubCategory.objects.all().delete()

categories_data = {
    "Skincare": ["Cleansers", "Face Wash", "Toners", "Serums", "Moisturizers", "Sunscreen", "Face Masks", "Eye Care", "Lip Care", "Exfoliators"],
    "Haircare": ["Shampoo", "Conditioner", "Hair Oil", "Hair Serum", "Hair Mask", "Scalp Care"],
    "Makeup": ["Foundation", "Concealer", "Lipstick", "Lip Gloss", "Blush", "Highlighter", "Mascara", "Eyeliner", "Eyeshadow", "Primer"],
    "Body Care": ["Body Wash", "Body Lotion", "Body Scrub", "Hand Care", "Foot Care"],
    "Fragrance": ["Perfume", "Body Mist", "Roll-On", "Fragrance Sets"],
    "Wellness": []
}

for cat_name, subcats in categories_data.items():
    cat = Category.objects.create(title=cat_name, slug=slugify(cat_name), status="Enabled")
    for subcat_name in subcats:
        SubCategory.objects.create(category=cat, title=subcat_name, slug=slugify(subcat_name), status="Enabled")

print("Seeded new cosmetics categories.")
