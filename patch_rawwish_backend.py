import os
import re

# 1. Update dash/models.py
models_path = 'dash/models.py'
with open(models_path, 'r') as f:
    content = f.read()

# Replace KTCS with RWCS
content = content.replace('KTCS', 'RWCS')

# Add Cosmetics Product Attributes models before Product
attr_models = """
class ProductAttribute(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class ProductAttributeValue(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='attributes')
    attribute = models.ForeignKey(ProductAttribute, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.product.name} - {self.attribute.name}: {self.value}"
"""

if 'class ProductAttribute' not in content:
    content = content.replace('class Product(models.Model):', attr_models + '\nclass Product(models.Model):')

# Enhance Variant
variant_additions = """    # Cosmetics Variant enhancements
    shade_name = models.CharField(max_length=255, blank=True, null=True)
    shade_code = models.CharField(max_length=50, blank=True, null=True)
    shade_family = models.CharField(max_length=100, blank=True, null=True)
    shade_hex = models.CharField(max_length=7, blank=True, null=True)
    volume = models.CharField(max_length=50, blank=True, null=True)
    pack_size = models.CharField(max_length=50, blank=True, null=True)
"""
if 'shade_name = models.CharField' not in content:
    content = content.replace('    image = models.ImageField(upload_to=\'variant_images/\', null=True, blank=True)',
                              '    image = models.ImageField(upload_to=\'variant_images/\', null=True, blank=True)\n' + variant_additions)

# Enhance ProductImage
image_type_additions = """    IMAGE_TYPES = [
        ('Primary', 'Primary'),
        ('Gallery', 'Gallery'),
        ('Lifestyle', 'Lifestyle'),
        ('Shade Swatch', 'Shade Swatch'),
        ('Ingredients', 'Ingredients'),
        ('How To Use', 'How To Use'),
        ('Texture', 'Texture'),
        ('Packaging', 'Packaging')
    ]
    image_type = models.CharField(max_length=50, choices=IMAGE_TYPES, default='Gallery')
    display_order = models.PositiveIntegerField(default=0)
"""
if 'image_type = models.CharField' not in content:
    content = content.replace("    image = models.ImageField(upload_to='product_images/')",
                              "    image = models.ImageField(upload_to='product_images/')\n" + image_type_additions)

with open(models_path, 'w') as f:
    f.write(content)

print("Updated dash/models.py")

# 2. Update main/views.py (Order ID generation)
main_views = 'main/views.py'
with open(main_views, 'r') as f:
    mv_content = f.read()

mv_content = mv_content.replace('f"#KT{date_str}{seq_val:05d}"', 'f"#RW{date_str}{seq_val:05d}"')

with open(main_views, 'w') as f:
    f.write(mv_content)

print("Updated main/views.py")

