import re

files_to_fix = [
    'template/dash/category/edit_category.html',
    'template/dash/product/add_product.html',
    'template/dash/product/edit_product.html',
    'template/dash/subcategory/edit_sub_category.html',
    'template/dash/subcategory/add_sub_category.html'
]

replacements = {
    "Shop our freshly ground Coorg cosmetics powder. Perfect for South Indian filter routine. Order online at Raw Wish.": "Shop our hydrating Vitamin C serum. Perfect for your morning skincare routine. Order online at Raw Wish.",
    "filter cosmetics, Coorg cosmetics, South Indian filter, Raw Wish": "hydrating serum, vitamin c, skincare routine, Raw Wish",
    "e.g. Slow shadeing process at Coorg estate": "e.g. Dermatologically tested for sensitive skin",
    "Update it when you add new products, change the grind focus, or run a promotion. Example for <strong>Cold Routine Ground Cosmetics</strong>:": "Update it when you add new products, change the skincare focus, or run a promotion. Example for <strong>Hydrating Face Serums</strong>:",
    '"Shop coarse ground cold routine cosmetics online at Raw Wish. Sourced from Chikmagalur estates. Smooth, low-acid routine at home."': '"Shop lightweight hydrating serums online at Raw Wish. Formulated with Hyaluronic Acid. Smooth, glowing skin at home."',
    "Use a grind-specific image — for example, a pour over setup for <strong>Pour Over Ground Cosmetics</strong> or a French press for <strong>French Press Ground Cosmetics</strong>.": "Use a product-specific image — for example, a swatches graphic for <strong>Lipsticks</strong> or a texture shot for <strong>Face Serums</strong>.",
    "Yes, especially if you have added new products or want to target new search terms. For <strong>Single Origin Ground Cosmetics</strong>, keep keywords like: <em>Coorg ground cosmetics, Chikmagalur cosmetics powder, Araku valley cosmetics, single estate ground cosmetics India, Raw Wish single origin</em>.": "Yes, especially if you have added new products or want to target new search terms. For <strong>Vitamin C Skincare</strong>, keep keywords like: <em>brightening serum, glowing skin cream, vitamin c face wash, anti-aging skincare India, Raw Wish vitamin c</em>.",
    "<li><em>Single Origin Cosmetics – Coorg & Chikmagalur | Raw Wish</em></li>": "<li><em>Vitamin C Skincare Collection – Serums & Creams | Raw Wish</em></li>",
    "<li><strong>Single Origin:</strong> Coorg cosmetics, Chikmagalur ground cosmetics, Araku valley cosmetics, single estate cosmetics India</li>": "<li><strong>Vitamin C:</strong> brightening serum, glowing skin cream, vitamin c face wash, anti-aging skincare India</li>",
}

for file_path in files_to_fix:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old, new in replacements.items():
        content = content.replace(old, new)
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Placeholders fixed.")
