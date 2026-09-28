"""
RAW WISH — PRODUCT CATALOGUE SEEDER
====================================

Creates:
    - 4 Categories
    - 8 Subcategories
    - 12 Products
    - Product Attributes
    - Product Attribute Values
    - Product Variants
    - Product Highlights

No images are created.

Designed for:
    Django + PostgreSQL

Run with:
    python manage.py shell < product_seed.py

OR:

    python manage.py shell
    >>> exec(open("product_seed.py").read())

IMPORTANT:
    This script is intentionally idempotent.
    Running it again will update/reuse existing records rather than
    blindly creating duplicates.
"""
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rawwish.settings")
django.setup()

from decimal import Decimal

from django.db import transaction
from django.utils.text import slugify

from dash.models import (
    Category,
    SubCategory,
    Product,
    ProductAttribute,
    ProductAttributeValue,
    Variant,
    Highlight,
)


# ============================================================
# CONFIGURATION
# ============================================================

DEFAULT_STATUS = "Enabled"

# Current catalogue assumptions.
# These are intentionally explicit so they can be changed easily.
DEFAULT_GST = Decimal("18.00")


# ============================================================
# CATEGORY DATA
# ============================================================

CATEGORIES = {
    "skincare": {
        "title": "Skincare",
        "description": (
            "Thoughtfully formulated skincare essentials designed to support "
            "healthy-looking, hydrated and balanced skin. Explore everyday "
            "cleansers, serums and targeted skincare solutions from Raw Wish."
        ),
        "meta_title": "Skincare Products for Healthy, Radiant Skin | Raw Wish",
        "meta_description": (
            "Shop Raw Wish skincare essentials including gentle cleansers "
            "and targeted serums designed for hydration, brightness and "
            "everyday skin care."
        ),
        "meta_keywords": (
            "skincare, skincare products, face care, face cleanser, serum, "
            "hydrating skincare, brightening skincare, Raw Wish"
        ),
    },

    "haircare": {
        "title": "Haircare",
        "description": (
            "Everyday haircare essentials created to cleanse, nourish and "
            "support healthier-looking hair and scalp. Discover shampoos and "
            "hair oils designed for modern haircare routines."
        ),
        "meta_title": "Haircare Products for Healthy-Looking Hair | Raw Wish",
        "meta_description": (
            "Explore Raw Wish haircare essentials including nourishing "
            "shampoos and hair oils for everyday hair and scalp care."
        ),
        "meta_keywords": (
            "haircare, hair care products, shampoo, hair oil, scalp care, "
            "nourishing haircare, Raw Wish"
        ),
    },

    "makeup": {
        "title": "Makeup",
        "description": (
            "Modern makeup essentials designed to complement everyday looks "
            "with comfortable textures, versatile shades and wearable finishes."
        ),
        "meta_title": "Makeup Products & Beauty Essentials | Raw Wish",
        "meta_description": (
            "Discover Raw Wish makeup essentials including lip colours and "
            "face makeup designed for comfortable, versatile everyday looks."
        ),
        "meta_keywords": (
            "makeup, makeup products, lipstick, lip colour, face makeup, "
            "beauty products, Raw Wish"
        ),
    },

    "body-care": {
        "title": "Body Care",
        "description": (
            "Simple, sensorial body care essentials created to cleanse, "
            "hydrate and leave skin feeling comfortable and cared for."
        ),
        "meta_title": "Body Care Products for Everyday Skin Care | Raw Wish",
        "meta_description": (
            "Shop Raw Wish body care essentials including body washes and "
            "body lotions designed for everyday cleansing and hydration."
        ),
        "meta_keywords": (
            "body care, body wash, body lotion, moisturiser, body moisturiser, "
            "hydrating body care, Raw Wish"
        ),
    },
}


# ============================================================
# SUBCATEGORY DATA
# ============================================================

SUBCATEGORIES = {
    "cleansers": {
        "category": "skincare",
        "title": "Cleansers",
        "description": (
            "Gentle facial cleansers designed to remove everyday impurities "
            "without leaving the skin feeling unnecessarily dry or tight."
        ),
        "meta_title": "Face Cleansers & Face Wash | Raw Wish",
        "meta_description": (
            "Discover Raw Wish face cleansers designed for gentle everyday "
            "cleansing and comfortable, refreshed-looking skin."
        ),
        "meta_keywords": (
            "face cleanser, facial cleanser, face wash, gentle cleanser, "
            "skincare cleanser, Raw Wish"
        ),
    },

    "serums": {
        "category": "skincare",
        "title": "Serums",
        "description": (
            "Targeted facial serums formulated around focused skincare needs "
            "such as hydration, brightening and balancing the appearance of skin."
        ),
        "meta_title": "Face Serums for Hydration & Brightening | Raw Wish",
        "meta_description": (
            "Explore Raw Wish facial serums for targeted skincare routines, "
            "including hydration, brightening and skin-balancing formulas."
        ),
        "meta_keywords": (
            "face serum, vitamin c serum, niacinamide serum, hyaluronic acid, "
            "hydrating serum, brightening serum, Raw Wish"
        ),
    },

    "shampoos": {
        "category": "haircare",
        "title": "Shampoos",
        "description": (
            "Everyday shampoos designed to cleanse the hair and scalp while "
            "supporting a comfortable and well-maintained haircare routine."
        ),
        "meta_title": "Shampoo for Everyday Hair & Scalp Care | Raw Wish",
        "meta_description": (
            "Shop Raw Wish shampoos designed for effective everyday cleansing "
            "and healthier-looking, manageable hair."
        ),
        "meta_keywords": (
            "shampoo, hair shampoo, scalp cleansing, everyday shampoo, "
            "haircare, Raw Wish"
        ),
    },

    "hair-oils": {
        "category": "haircare",
        "title": "Hair Oils",
        "description": (
            "Nourishing hair and scalp oils designed to complement regular "
            "haircare routines with lightweight botanical-inspired care."
        ),
        "meta_title": "Hair Oils for Nourishment & Scalp Care | Raw Wish",
        "meta_description": (
            "Explore Raw Wish hair oils designed to nourish hair and support "
            "a simple, consistent scalp and haircare routine."
        ),
        "meta_keywords": (
            "hair oil, scalp oil, nourishing hair oil, rosemary hair oil, "
            "hair nourishment, Raw Wish"
        ),
    },

    "lip-makeup": {
        "category": "makeup",
        "title": "Lip Makeup",
        "description": (
            "Wearable lip colours with comfortable textures and versatile "
            "shades designed for everyday makeup looks."
        ),
        "meta_title": "Lipsticks & Lip Colours | Raw Wish",
        "meta_description": (
            "Discover Raw Wish lip makeup with wearable shades, comfortable "
            "textures and finishes for everyday beauty looks."
        ),
        "meta_keywords": (
            "lipstick, lip colour, lip makeup, matte lipstick, lip tint, "
            "beauty makeup, Raw Wish"
        ),
    },

    "face-makeup": {
        "category": "makeup",
        "title": "Face Makeup",
        "description": (
            "Everyday face makeup essentials designed to help create "
            "comfortable, polished and versatile makeup looks."
        ),
        "meta_title": "Face Makeup & Beauty Essentials | Raw Wish",
        "meta_description": (
            "Explore Raw Wish face makeup essentials designed for versatile "
            "everyday beauty looks and comfortable wear."
        ),
        "meta_keywords": (
            "face makeup, makeup essentials, foundation, concealer, "
            "face beauty, Raw Wish"
        ),
    },

    "body-wash": {
        "category": "body-care",
        "title": "Body Wash",
        "description": (
            "Gentle and sensorial body cleansers designed for refreshing "
            "everyday showers while helping skin feel clean and comfortable."
        ),
        "meta_title": "Body Wash for Everyday Cleansing | Raw Wish",
        "meta_description": (
            "Shop Raw Wish body washes designed for refreshing everyday "
            "cleansing and comfortable-feeling skin."
        ),
        "meta_keywords": (
            "body wash, shower gel, body cleanser, bathing, body care, "
            "Raw Wish"
        ),
    },

    "body-lotion": {
        "category": "body-care",
        "title": "Body Lotion",
        "description": (
            "Daily body moisturisers designed to replenish moisture and leave "
            "skin feeling soft, smooth and comfortable."
        ),
        "meta_title": "Body Lotion & Daily Body Moisturiser | Raw Wish",
        "meta_description": (
            "Discover Raw Wish body lotions designed for everyday hydration "
            "and soft, smooth-feeling skin."
        ),
        "meta_keywords": (
            "body lotion, body moisturiser, body cream, hydrating lotion, "
            "body hydration, Raw Wish"
        ),
    },
}


# ============================================================
# PRODUCT DATA
# ============================================================

PRODUCTS = [
    {
        "key": "gentle-hydrating-face-cleanser",
        "category": "skincare",
        "subcategory": "cleansers",
        "name": "Gentle Hydrating Face Cleanser",
        "description": (
            "A gentle daily face cleanser designed to remove dirt, excess "
            "oil and everyday impurities while helping skin feel comfortable "
            "and refreshed. The creamy gel texture is suitable for a simple "
            "morning and evening skincare routine."
        ),
        "meta_title": "Gentle Hydrating Face Cleanser 100 ml | Raw Wish",
        "meta_description": (
            "Shop Raw Wish Gentle Hydrating Face Cleanser, a comfortable "
            "daily cleanser designed to remove impurities without leaving "
            "skin feeling stripped."
        ),
        "meta_keywords": (
            "gentle face cleanser, hydrating face wash, daily cleanser, "
            "face wash, sensitive skin cleanser, Raw Wish"
        ),
        "highlights": [
            "Gentle everyday cleansing",
            "Comfortable gel texture",
            "Helps remove excess oil and impurities",
            "Suitable for morning and evening routines",
        ],
        "attributes": {
            "Skin Type": "Normal to dry",
            "Skin Concern": "Dryness and dullness",
            "Texture": "Creamy gel",
            "Key Ingredients": "Glycerin, Panthenol, Aloe Vera",
            "Benefits": "Cleanses, refreshes and supports comfortable-looking skin",
            "How To Use": "Massage onto damp skin and rinse thoroughly. Use morning and evening.",
            "Suitable For": "Normal, dry and combination skin",
            "Formulation": "Gel cleanser",
        },
        "variants": [
            {
                "name": "100 ml",
                "quantity": 120,
                "price": "349.00",
                "gst": "18.00",
                "volume": "100 ml",
                "weight": "0.13",
                "length": "5.00",
                "breadth": "5.00",
                "height": "15.00",
            }
        ],
    },

    {
        "key": "vitamin-c-brightening-serum",
        "category": "skincare",
        "subcategory": "serums",
        "name": "Vitamin C Brightening Serum",
        "description": (
            "A lightweight facial serum formulated with Vitamin C and "
            "supportive humectants to complement a brightening-focused "
            "skincare routine. Designed to leave skin looking fresh, smooth "
            "and visibly more radiant with consistent use."
        ),
        "meta_title": "Vitamin C Brightening Serum 30 ml | Raw Wish",
        "meta_description": (
            "Discover Raw Wish Vitamin C Brightening Serum, a lightweight "
            "daily serum designed to support a brighter, fresher-looking complexion."
        ),
        "meta_keywords": (
            "vitamin c serum, brightening serum, face serum, radiant skin, "
            "vitamin c skincare, Raw Wish"
        ),
        "highlights": [
            "Lightweight serum texture",
            "Brightening-focused formula",
            "Designed for everyday skincare routines",
            "Helps support a fresh-looking complexion",
        ],
        "attributes": {
            "Skin Type": "Normal, combination and oily",
            "Skin Concern": "Dullness and uneven-looking tone",
            "Texture": "Lightweight serum",
            "Key Ingredients": "Vitamin C, Hyaluronic Acid, Vitamin E",
            "Benefits": "Supports brighter and more radiant-looking skin",
            "How To Use": "Apply 2–3 drops to clean, dry skin before moisturiser. Use sunscreen during the day.",
            "Suitable For": "Normal, combination and oily skin",
            "Formulation": "Water-based serum",
        },
        "variants": [
            {
                "name": "30 ml",
                "quantity": 90,
                "price": "699.00",
                "gst": "18.00",
                "volume": "30 ml",
                "weight": "0.08",
                "length": "4.00",
                "breadth": "4.00",
                "height": "11.00",
            }
        ],
    },

    {
        "key": "niacinamide-zinc-serum",
        "category": "skincare",
        "subcategory": "serums",
        "name": "Niacinamide + Zinc Balancing Serum",
        "description": (
            "A lightweight balancing serum featuring Niacinamide and Zinc "
            "to complement routines focused on excess oil and uneven-looking "
            "skin. The fast-absorbing texture layers easily under moisturiser."
        ),
        "meta_title": "Niacinamide + Zinc Balancing Serum 30 ml | Raw Wish",
        "meta_description": (
            "Shop Raw Wish Niacinamide + Zinc Balancing Serum for lightweight "
            "daily skincare focused on oil balance and a smoother-looking complexion."
        ),
        "meta_keywords": (
            "niacinamide serum, zinc serum, oily skin serum, balancing serum, "
            "acne prone skin care, Raw Wish"
        ),
        "highlights": [
            "Lightweight fast-absorbing texture",
            "Designed for oil-balancing routines",
            "Helps support smoother-looking skin",
            "Easy to layer under moisturiser",
        ],
        "attributes": {
            "Skin Type": "Combination and oily",
            "Skin Concern": "Excess oil and uneven-looking texture",
            "Texture": "Lightweight serum",
            "Key Ingredients": "Niacinamide, Zinc PCA, Panthenol",
            "Benefits": "Supports balanced and smoother-looking skin",
            "How To Use": "Apply 2–3 drops to clean skin and follow with moisturiser.",
            "Suitable For": "Combination and oily skin",
            "Formulation": "Water-based serum",
        },
        "variants": [
            {
                "name": "30 ml",
                "quantity": 85,
                "price": "649.00",
                "gst": "18.00",
                "volume": "30 ml",
                "weight": "0.08",
                "length": "4.00",
                "breadth": "4.00",
                "height": "11.00",
            }
        ],
    },

    {
        "key": "daily-nourishing-shampoo",
        "category": "haircare",
        "subcategory": "shampoos",
        "name": "Daily Nourishing Shampoo",
        "description": (
            "A gentle everyday shampoo designed to cleanse the scalp and "
            "hair while helping maintain a soft, manageable feel. Suitable "
            "for regular washing as part of a simple haircare routine."
        ),
        "meta_title": "Daily Nourishing Shampoo 250 ml | Raw Wish",
        "meta_description": (
            "Shop Raw Wish Daily Nourishing Shampoo, a gentle everyday "
            "formula designed to cleanse hair while supporting a soft, manageable feel."
        ),
        "meta_keywords": (
            "nourishing shampoo, daily shampoo, gentle shampoo, hair cleanser, "
            "haircare, Raw Wish"
        ),
        "highlights": [
            "Gentle everyday cleansing",
            "Helps maintain manageable hair",
            "Suitable for regular washing",
            "Fresh, lightweight finish",
        ],
        "attributes": {
            "Hair Type": "Normal to dry",
            "Hair Concern": "Dryness and roughness",
            "Texture": "Liquid gel",
            "Key Ingredients": "Aloe Vera, Panthenol, Glycerin",
            "Benefits": "Cleanses while supporting soft, manageable-looking hair",
            "How To Use": "Apply to wet scalp and hair, massage gently and rinse thoroughly.",
            "Suitable For": "Regular use",
            "Formulation": "Liquid shampoo",
        },
        "variants": [
            {
                "name": "250 ml",
                "quantity": 100,
                "price": "499.00",
                "gst": "18.00",
                "volume": "250 ml",
                "weight": "0.30",
                "length": "6.00",
                "breadth": "6.00",
                "height": "18.00",
            }
        ],
    },

    {
        "key": "anti-frizz-smoothing-shampoo",
        "category": "haircare",
        "subcategory": "shampoos",
        "name": "Anti-Frizz Smoothing Shampoo",
        "description": (
            "A smoothing shampoo created for hair that feels dry, rough or "
            "difficult to manage. Its creamy cleansing texture helps leave "
            "hair feeling cleaner, softer and easier to style."
        ),
        "meta_title": "Anti-Frizz Smoothing Shampoo 250 ml | Raw Wish",
        "meta_description": (
            "Discover Raw Wish Anti-Frizz Smoothing Shampoo for dry, rough and "
            "frizz-prone hair, designed for smoother and more manageable-looking hair."
        ),
        "meta_keywords": (
            "anti frizz shampoo, smoothing shampoo, frizzy hair, dry hair "
            "shampoo, hair smoothing, Raw Wish"
        ),
        "highlights": [
            "Designed for frizz-prone hair",
            "Creamy cleansing texture",
            "Helps improve manageability",
            "Suitable for regular haircare routines",
        ],
        "attributes": {
            "Hair Type": "Wavy, curly and dry",
            "Hair Concern": "Frizz and roughness",
            "Texture": "Creamy liquid",
            "Key Ingredients": "Argan Oil, Shea Butter, Panthenol",
            "Benefits": "Supports softer and more manageable-looking hair",
            "How To Use": "Massage into wet hair and scalp. Rinse thoroughly and follow with conditioner.",
            "Suitable For": "Dry, wavy and frizz-prone hair",
            "Formulation": "Smoothing shampoo",
        },
        "variants": [
            {
                "name": "250 ml",
                "quantity": 80,
                "price": "549.00",
                "gst": "18.00",
                "volume": "250 ml",
                "weight": "0.30",
                "length": "6.00",
                "breadth": "6.00",
                "height": "18.00",
            }
        ],
    },

    {
        "key": "rosemary-scalp-hair-oil",
        "category": "haircare",
        "subcategory": "hair-oils",
        "name": "Rosemary Scalp & Hair Oil",
        "description": (
            "A lightweight botanical-inspired hair oil designed to complement "
            "regular scalp massage and hair nourishment routines. The blend "
            "combines rosemary with nourishing plant oils for a comfortable "
            "pre-wash treatment."
        ),
        "meta_title": "Rosemary Scalp & Hair Oil 100 ml | Raw Wish",
        "meta_description": (
            "Shop Raw Wish Rosemary Scalp & Hair Oil, a lightweight pre-wash "
            "oil designed to complement scalp massage and hair nourishment routines."
        ),
        "meta_keywords": (
            "rosemary hair oil, scalp oil, hair nourishment, rosemary oil "
            "for hair, hair oil, Raw Wish"
        ),
        "highlights": [
            "Lightweight oil blend",
            "Ideal for scalp massage",
            "Designed for pre-wash routines",
            "Nourishing botanical-inspired formula",
        ],
        "attributes": {
            "Hair Type": "Normal, dry and wavy",
            "Hair Concern": "Dryness and roughness",
            "Texture": "Lightweight oil",
            "Key Ingredients": "Rosemary Extract, Coconut Oil, Jojoba Oil",
            "Benefits": "Helps nourish hair and supports a comfortable scalp-care routine",
            "How To Use": "Massage a small amount into scalp and lengths. Leave for 30–60 minutes before shampooing.",
            "Suitable For": "Regular pre-wash haircare",
            "Formulation": "Oil blend",
        },
        "variants": [
            {
                "name": "100 ml",
                "quantity": 110,
                "price": "599.00",
                "gst": "18.00",
                "volume": "100 ml",
                "weight": "0.13",
                "length": "5.00",
                "breadth": "5.00",
                "height": "15.00",
            }
        ],
    },

    {
        "key": "velvet-matte-lip-colour",
        "category": "makeup",
        "subcategory": "lip-makeup",
        "name": "Velvet Matte Lip Colour",
        "description": (
            "A comfortable matte lip colour with a smooth, buildable texture "
            "designed for everyday wear. The formula glides evenly across the "
            "lips and can be layered for a more intense finish."
        ),
        "meta_title": "Velvet Matte Lip Colour | Long-Wear Lipstick | Raw Wish",
        "meta_description": (
            "Discover Raw Wish Velvet Matte Lip Colour with comfortable, "
            "buildable coverage and wearable shades designed for everyday makeup."
        ),
        "meta_keywords": (
            "matte lipstick, velvet lipstick, lip colour, long wear lipstick, "
            "matte lip makeup, Raw Wish"
        ),
        "highlights": [
            "Comfortable matte finish",
            "Buildable colour payoff",
            "Smooth application",
            "Wearable everyday shades",
        ],
        "attributes": {
            "Finish": "Velvet matte",
            "Texture": "Creamy",
            "Coverage": "Buildable",
            "Key Ingredients": "Jojoba Oil, Vitamin E",
            "Benefits": "Provides buildable colour with a comfortable matte finish",
            "How To Use": "Apply directly to lips. Layer for increased colour intensity.",
            "Suitable For": "Everyday and occasion makeup",
            "Formulation": "Cream lipstick",
        },
        "variants": [
            {
                "name": "Nude Rose",
                "quantity": 60,
                "price": "799.00",
                "gst": "18.00",
                "shade_name": "Nude Rose",
                "shade_code": "RW-L01",
                "shade_family": "Nude",
                "shade_hex": "#B76E79",
                "volume": "3.8 g",
                "weight": "0.07",
                "length": "2.50",
                "breadth": "2.50",
                "height": "9.00",
            },
            {
                "name": "Berry Wine",
                "quantity": 55,
                "price": "799.00",
                "gst": "18.00",
                "shade_name": "Berry Wine",
                "shade_code": "RW-L02",
                "shade_family": "Berry",
                "shade_hex": "#7A263A",
                "volume": "3.8 g",
                "weight": "0.07",
                "length": "2.50",
                "breadth": "2.50",
                "height": "9.00",
            },
            {
                "name": "Warm Mocha",
                "quantity": 50,
                "price": "799.00",
                "gst": "18.00",
                "shade_name": "Warm Mocha",
                "shade_code": "RW-L03",
                "shade_family": "Brown",
                "shade_hex": "#8B5E4A",
                "volume": "3.8 g",
                "weight": "0.07",
                "length": "2.50",
                "breadth": "2.50",
                "height": "9.00",
            },
        ],
    },

    {
        "key": "hydrating-lip-tint",
        "category": "makeup",
        "subcategory": "lip-makeup",
        "name": "Hydrating Lip Tint",
        "description": (
            "A lightweight lip tint designed to add a sheer wash of colour "
            "while keeping the lips feeling comfortable. Build the colour "
            "gradually for a soft everyday look."
        ),
        "meta_title": "Hydrating Lip Tint | Sheer Everyday Lip Colour | Raw Wish",
        "meta_description": (
            "Shop Raw Wish Hydrating Lip Tint for lightweight, buildable "
            "colour and a comfortable everyday lip look."
        ),
        "meta_keywords": (
            "lip tint, hydrating lip tint, sheer lip colour, tinted lip, "
            "everyday lip makeup, Raw Wish"
        ),
        "highlights": [
            "Lightweight sheer colour",
            "Buildable intensity",
            "Comfortable everyday finish",
            "Easy-to-layer formula",
        ],
        "attributes": {
            "Finish": "Natural",
            "Texture": "Lightweight tint",
            "Coverage": "Sheer to buildable",
            "Key Ingredients": "Hyaluronic Acid, Vitamin E, Squalane",
            "Benefits": "Adds buildable colour with a comfortable finish",
            "How To Use": "Apply directly to lips and layer for increased colour intensity.",
            "Suitable For": "Everyday makeup",
            "Formulation": "Liquid lip tint",
        },
        "variants": [
            {
                "name": "Rose Petal",
                "quantity": 65,
                "price": "599.00",
                "gst": "18.00",
                "shade_name": "Rose Petal",
                "shade_code": "RW-T01",
                "shade_family": "Rose",
                "shade_hex": "#C86F7D",
                "volume": "5 ml",
                "weight": "0.06",
                "length": "2.50",
                "breadth": "2.50",
                "height": "10.00",
            },
            {
                "name": "Cherry Flush",
                "quantity": 60,
                "price": "599.00",
                "gst": "18.00",
                "shade_name": "Cherry Flush",
                "shade_code": "RW-T02",
                "shade_family": "Red",
                "shade_hex": "#B83B4B",
                "volume": "5 ml",
                "weight": "0.06",
                "length": "2.50",
                "breadth": "2.50",
                "height": "10.00",
            },
        ],
    },

    {
        "key": "daily-hydration-body-wash",
        "category": "body-care",
        "subcategory": "body-wash",
        "name": "Daily Hydration Body Wash",
        "description": (
            "A refreshing body wash designed for everyday cleansing with a "
            "soft lather and comfortable after-feel. Ideal for a simple daily "
            "shower routine."
        ),
        "meta_title": "Daily Hydration Body Wash 300 ml | Raw Wish",
        "meta_description": (
            "Discover Raw Wish Daily Hydration Body Wash, a refreshing "
            "everyday cleanser designed to leave skin feeling clean and comfortable."
        ),
        "meta_keywords": (
            "body wash, hydrating body wash, shower gel, daily body cleanser, "
            "body care, Raw Wish"
        ),
        "highlights": [
            "Refreshing everyday cleanse",
            "Soft lather",
            "Comfortable after-feel",
            "Suitable for daily use",
        ],
        "attributes": {
            "Skin Type": "All skin types",
            "Skin Concern": "Dryness",
            "Texture": "Gel",
            "Key Ingredients": "Glycerin, Aloe Vera, Panthenol",
            "Benefits": "Cleanses while helping skin feel comfortable and refreshed",
            "How To Use": "Apply to wet skin, massage into a gentle lather and rinse thoroughly.",
            "Suitable For": "Daily use",
            "Fragrance": "Fresh botanical",
            "Formulation": "Body cleansing gel",
        },
        "variants": [
            {
                "name": "300 ml",
                "quantity": 95,
                "price": "449.00",
                "gst": "18.00",
                "volume": "300 ml",
                "weight": "0.36",
                "length": "6.50",
                "breadth": "6.50",
                "height": "20.00",
            }
        ],
    },

    {
        "key": "shea-butter-body-lotion",
        "category": "body-care",
        "subcategory": "body-lotion",
        "name": "Shea Butter Body Lotion",
        "description": (
            "A rich yet comfortable daily body lotion formulated with Shea "
            "Butter and nourishing emollients to help replenish moisture and "
            "leave skin feeling soft and smooth."
        ),
        "meta_title": "Shea Butter Body Lotion 250 ml | Raw Wish",
        "meta_description": (
            "Shop Raw Wish Shea Butter Body Lotion for rich daily hydration "
            "and soft, smooth-feeling skin."
        ),
        "meta_keywords": (
            "shea butter body lotion, body lotion, moisturiser, dry skin "
            "lotion, hydrating body lotion, Raw Wish"
        ),
        "highlights": [
            "Rich moisturising texture",
            "Designed for dry-feeling skin",
            "Helps maintain soft, smooth-feeling skin",
            "Ideal for everyday body care",
        ],
        "attributes": {
            "Skin Type": "Normal to dry",
            "Skin Concern": "Dryness and roughness",
            "Texture": "Rich lotion",
            "Key Ingredients": "Shea Butter, Squalane, Glycerin",
            "Benefits": "Helps replenish moisture and maintain soft-feeling skin",
            "How To Use": "Massage generously onto clean, dry skin. Reapply to dry areas as needed.",
            "Suitable For": "Normal and dry skin",
            "Fragrance": "Soft warm botanical",
            "Formulation": "Moisturising lotion",
        },
        "variants": [
            {
                "name": "250 ml",
                "quantity": 90,
                "price": "549.00",
                "gst": "18.00",
                "volume": "250 ml",
                "weight": "0.30",
                "length": "6.50",
                "breadth": "6.50",
                "height": "18.00",
            }
        ],
    },

    {
        "key": "hyaluronic-acid-hydration-serum",
        "category": "skincare",
        "subcategory": "serums",
        "name": "Hyaluronic Acid Hydration Serum",
        "description": (
            "A lightweight hydration serum formulated with Hyaluronic Acid "
            "and humectants to help skin feel replenished, comfortable and "
            "fresh. Designed to layer easily within morning and evening routines."
        ),
        "meta_title": "Hyaluronic Acid Hydration Serum 30 ml | Raw Wish",
        "meta_description": (
            "Shop Raw Wish Hyaluronic Acid Hydration Serum for lightweight "
            "daily hydration and a fresh, comfortable-looking complexion."
        ),
        "meta_keywords": (
            "hyaluronic acid serum, hydrating serum, face hydration, "
            "hydration serum, dry skin serum, Raw Wish"
        ),
        "highlights": [
            "Lightweight hydration",
            "Easy to layer",
            "Helps skin feel replenished",
            "Suitable for morning and evening routines",
        ],
        "attributes": {
            "Skin Type": "All skin types",
            "Skin Concern": "Dehydration",
            "Texture": "Lightweight gel serum",
            "Key Ingredients": "Hyaluronic Acid, Glycerin, Panthenol",
            "Benefits": "Helps support hydrated and comfortable-looking skin",
            "How To Use": "Apply 2–3 drops to slightly damp skin and follow with moisturiser.",
            "Suitable For": "All skin types",
            "Formulation": "Water-based serum",
        },
        "variants": [
            {
                "name": "30 ml",
                "quantity": 100,
                "price": "749.00",
                "gst": "18.00",
                "volume": "30 ml",
                "weight": "0.08",
                "length": "4.00",
                "breadth": "4.00",
                "height": "11.00",
            }
        ],
    },

    {
        "key": "rosemary-bhringraj-hair-oil",
        "category": "haircare",
        "subcategory": "hair-oils",
        "name": "Rosemary & Bhringraj Hair Oil",
        "description": (
            "A nourishing traditional-inspired hair oil blend combining "
            "Bhringraj with Rosemary and lightweight botanical oils. Designed "
            "for regular pre-wash scalp massage and hair nourishment."
        ),
        "meta_title": "Rosemary & Bhringraj Hair Oil 100 ml | Raw Wish",
        "meta_description": (
            "Discover Raw Wish Rosemary & Bhringraj Hair Oil, a nourishing "
            "botanical-inspired blend for regular scalp massage and haircare."
        ),
        "meta_keywords": (
            "bhringraj hair oil, rosemary hair oil, herbal hair oil, scalp "
            "massage oil, hair nourishment, Raw Wish"
        ),
        "highlights": [
            "Botanical-inspired hair oil",
            "Ideal for scalp massage",
            "Designed for pre-wash use",
            "Nourishing oil blend",
        ],
        "attributes": {
            "Hair Type": "Normal, dry and wavy",
            "Hair Concern": "Dryness and roughness",
            "Texture": "Medium-weight oil",
            "Key Ingredients": "Bhringraj Extract, Rosemary Extract, Sesame Oil, Coconut Oil",
            "Benefits": "Helps nourish hair and complement regular scalp-care routines",
            "How To Use": "Massage into scalp and hair lengths. Leave for 30–60 minutes before shampooing.",
            "Suitable For": "Regular pre-wash routines",
            "Formulation": "Botanical oil blend",
        },
        "variants": [
            {
                "name": "100 ml",
                "quantity": 100,
                "price": "499.00",
                "gst": "18.00",
                "volume": "100 ml",
                "weight": "0.13",
                "length": "5.00",
                "breadth": "5.00",
                "height": "15.00",
            }
        ],
    },

    {
        "key": "skin-perfecting-tinted-base",
        "category": "makeup",
        "subcategory": "face-makeup",
        "name": "Skin Perfecting Tinted Base",
        "description": (
            "A lightweight tinted face base designed to even the appearance "
            "of skin while maintaining a comfortable, natural-looking finish. "
            "The buildable formula works well for everyday makeup."
        ),
        "meta_title": "Skin Perfecting Tinted Base | Lightweight Face Makeup | Raw Wish",
        "meta_description": (
            "Discover Raw Wish Skin Perfecting Tinted Base with lightweight, "
            "buildable coverage and a natural-looking finish for everyday makeup."
        ),
        "meta_keywords": (
            "tinted base, skin tint, face makeup, lightweight foundation, "
            "natural finish makeup, Raw Wish"
        ),
        "highlights": [
            "Lightweight feel",
            "Buildable coverage",
            "Natural-looking finish",
            "Designed for everyday wear",
        ],
        "attributes": {
            "Finish": "Natural",
            "Texture": "Lightweight fluid",
            "Coverage": "Sheer to medium",
            "Key Ingredients": "Squalane, Vitamin E, Glycerin",
            "Benefits": "Helps even the appearance of skin with lightweight coverage",
            "How To Use": "Apply a small amount to the face and blend evenly using fingers, sponge or brush.",
            "Suitable For": "Everyday makeup",
            "Formulation": "Liquid face base",
        },
        "variants": [
            {
                "name": "Light",
                "quantity": 45,
                "price": "899.00",
                "gst": "18.00",
                "shade_name": "Light",
                "shade_code": "RW-B01",
                "shade_family": "Light",
                "shade_hex": "#E7C2A8",
                "volume": "30 ml",
                "weight": "0.08",
                "length": "4.00",
                "breadth": "4.00",
                "height": "12.00",
            },
            {
                "name": "Medium",
                "quantity": 50,
                "price": "899.00",
                "gst": "18.00",
                "shade_name": "Medium",
                "shade_code": "RW-B02",
                "shade_family": "Medium",
                "shade_hex": "#C98E68",
                "volume": "30 ml",
                "weight": "0.08",
                "length": "4.00",
                "breadth": "4.00",
                "height": "12.00",
            },
            {
                "name": "Deep",
                "quantity": 40,
                "price": "899.00",
                "gst": "18.00",
                "shade_name": "Deep",
                "shade_code": "RW-B03",
                "shade_family": "Deep",
                "shade_hex": "#75482F",
                "volume": "30 ml",
                "weight": "0.08",
                "length": "4.00",
                "breadth": "4.00",
                "height": "12.00",
            },
        ],
    },
]


# ============================================================
# HELPERS
# ============================================================

def get_or_create_category(data):
    slug = slugify(data["title"])

    category, created = Category.objects.get_or_create(
        slug=slug,
        defaults={
            "title": data["title"],
            "description": data["description"],
            "meta_title": data["meta_title"],
            "meta_description": data["meta_description"],
            "meta_keywords": data["meta_keywords"],
            "status": DEFAULT_STATUS,
        },
    )

    if not created:
        category.title = data["title"]
        category.description = data["description"]
        category.meta_title = data["meta_title"]
        category.meta_description = data["meta_description"]
        category.meta_keywords = data["meta_keywords"]
        category.status = DEFAULT_STATUS
        category.save()

    return category


def get_or_create_subcategory(data, category):
    slug = slugify(data["title"])

    subcategory, created = SubCategory.objects.get_or_create(
        category=category,
        slug=slug,
        defaults={
            "title": data["title"],
            "description": data["description"],
            "meta_title": data["meta_title"],
            "meta_description": data["meta_description"],
            "meta_keywords": data["meta_keywords"],
            "status": DEFAULT_STATUS,
        },
    )

    if not created:
        subcategory.title = data["title"]
        subcategory.description = data["description"]
        subcategory.meta_title = data["meta_title"]
        subcategory.meta_description = data["meta_description"]
        subcategory.meta_keywords = data["meta_keywords"]
        subcategory.status = DEFAULT_STATUS
        subcategory.save()

    return subcategory


def get_or_create_attribute(name, description=""):
    attribute, created = ProductAttribute.objects.get_or_create(
        name=name,
        defaults={
            "description": description,
        },
    )

    if not created and description and attribute.description != description:
        attribute.description = description
        attribute.save(update_fields=["description"])

    return attribute


def create_product_attribute(product, attribute_name, value):
    attribute = get_or_create_attribute(attribute_name)

    ProductAttributeValue.objects.update_or_create(
        product=product,
        attribute=attribute,
        defaults={
            "value": value,
        },
    )


def create_highlight(product, text):
    Highlight.objects.get_or_create(
        product=product,
        text=text,
    )


def create_variant(product, data):
    variant, created = Variant.objects.get_or_create(
        product=product,
        name=data["name"],
        defaults={
            "quantity": data["quantity"],
            "price": Decimal(data["price"]),
            "gst": Decimal(data.get("gst", DEFAULT_GST)),
            "shade_name": data.get("shade_name"),
            "shade_code": data.get("shade_code"),
            "shade_family": data.get("shade_family"),
            "shade_hex": data.get("shade_hex"),
            "volume": data.get("volume"),
            "pack_size": data.get("pack_size"),
            "status": DEFAULT_STATUS,
            "weight": Decimal(data.get("weight", "0.10")),
            "length": Decimal(data.get("length", "5.00")),
            "breadth": Decimal(data.get("breadth", "5.00")),
            "height": Decimal(data.get("height", "10.00")),
        },
    )

    if not created:
        variant.quantity = data["quantity"]
        variant.price = Decimal(data["price"])
        variant.gst = Decimal(data.get("gst", DEFAULT_GST))
        variant.shade_name = data.get("shade_name")
        variant.shade_code = data.get("shade_code")
        variant.shade_family = data.get("shade_family")
        variant.shade_hex = data.get("shade_hex")
        variant.volume = data.get("volume")
        variant.pack_size = data.get("pack_size")
        variant.status = DEFAULT_STATUS
        variant.weight = Decimal(data.get("weight", "0.10"))
        variant.length = Decimal(data.get("length", "5.00"))
        variant.breadth = Decimal(data.get("breadth", "5.00"))
        variant.height = Decimal(data.get("height", "10.00"))
        variant.save()

    return variant


# ============================================================
# MAIN SEEDER
# ============================================================

@transaction.atomic
def seed():
    print("\n" + "=" * 70)
    print("RAW WISH — PRODUCT CATALOGUE SEED")
    print("=" * 70)

    # --------------------------------------------------------
    # CATEGORIES
    # --------------------------------------------------------

    category_objects = {}

    print("\n[1/4] Creating categories...")

    for key, data in CATEGORIES.items():
        category = get_or_create_category(data)
        category_objects[key] = category

        print(
            f"  ✓ {category.title}"
            f"  | status={category.status}"
            f"  | slug={category.slug}"
        )

    # --------------------------------------------------------
    # SUBCATEGORIES
    # --------------------------------------------------------

    subcategory_objects = {}

    print("\n[2/4] Creating subcategories...")

    for key, data in SUBCATEGORIES.items():
        category = category_objects[data["category"]]

        subcategory = get_or_create_subcategory(
            data,
            category,
        )

        subcategory_objects[key] = subcategory

        print(
            f"  ✓ {category.title} → {subcategory.title}"
            f"  | slug={subcategory.slug}"
        )

    # --------------------------------------------------------
    # PRODUCTS
    # --------------------------------------------------------

    print("\n[3/4] Creating products, attributes and variants...")

    product_objects = {}

    for product_data in PRODUCTS:

        category = category_objects[product_data["category"]]
        subcategory = subcategory_objects[product_data["subcategory"]]

        slug = slugify(product_data["name"])

        product, created = Product.objects.get_or_create(
            slug=slug,
            defaults={
                "category": category,
                "sub_category": subcategory,
                "name": product_data["name"],
                "description": product_data["description"],
                "meta_title": product_data["meta_title"],
                "meta_description": product_data["meta_description"],
                "meta_keywords": product_data["meta_keywords"],
            },
        )

        if not created:
            product.category = category
            product.sub_category = subcategory
            product.name = product_data["name"]
            product.description = product_data["description"]
            product.meta_title = product_data["meta_title"]
            product.meta_description = product_data["meta_description"]
            product.meta_keywords = product_data["meta_keywords"]
            product.save()

        product_objects[product_data["key"]] = product

        print(
            f"\n  {'CREATED' if created else 'UPDATED'}: "
            f"{product.name}"
        )

        print(
            f"    Category    : {category.title}"
        )

        print(
            f"    Subcategory : {subcategory.title}"
        )

        print(
            f"    Slug        : {product.slug}"
        )

        # ----------------------------------------------------
        # ATTRIBUTES
        # ----------------------------------------------------

        for attribute_name, value in product_data.get(
            "attributes",
            {}
        ).items():

            create_product_attribute(
                product,
                attribute_name,
                value,
            )

            print(
                f"    Attribute   : {attribute_name} = {value}"
            )

        # ----------------------------------------------------
        # HIGHLIGHTS
        # ----------------------------------------------------

        for highlight_text in product_data.get(
            "highlights",
            []
        ):
            create_highlight(
                product,
                highlight_text,
            )

        # ----------------------------------------------------
        # VARIANTS
        # ----------------------------------------------------

        for variant_data in product_data.get(
            "variants",
            []
        ):

            variant = create_variant(
                product,
                variant_data,
            )

            print(
                f"    Variant     : {variant.name}"
                f" | ₹{variant.price}"
                f" | GST {variant.gst}%"
                f" | Stock {variant.quantity}"
            )

    # --------------------------------------------------------
    # FINAL SUMMARY
    # --------------------------------------------------------

    print("\n[4/4] Catalogue verification...")

    print(
        f"  Categories       : {Category.objects.count()}"
    )

    print(
        f"  Subcategories    : {SubCategory.objects.count()}"
    )

    print(
        f"  Products         : {Product.objects.count()}"
    )

    print(
        f"  Attributes       : {ProductAttribute.objects.count()}"
    )

    print(
        f"  Attribute Values : {ProductAttributeValue.objects.count()}"
    )

    print(
        f"  Variants         : {Variant.objects.count()}"
    )

    print(
        f"  Highlights       : {Highlight.objects.count()}"
    )

    print("\n" + "=" * 70)
    print("RAW WISH CATALOGUE SEED COMPLETED SUCCESSFULLY")
    print("=" * 70)

    print("\nImages were intentionally NOT created.")
    print("You can add product/category/variant images later.")
    print("\n")


# ============================================================
# EXECUTE
# ============================================================

if __name__ == "__main__":
    seed()

