import os
import re

CSS_REPLACEMENTS = {
    '--rawwish-espresso': '--rw-dark',
    '--rawwish-dark-roast': '--rw-medium',
    '--rawwish-red-oxide': '--rw-primary',
    'kt-': 'rw-',
    'Kapi': 'Rawwish',
    'kapi': 'rawwish',
    'coffee': 'cosmetics',
    'Coffee': 'Cosmetics',
    'brew': 'routine',
    'Brew': 'Routine',
    'roast': 'shade',
    'Roast': 'Shade'
}

def patch_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = content
        for k, v in CSS_REPLACEMENTS.items():
            new_content = new_content.replace(k, v)
            
        if content != new_content:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_content)
    except:
        pass

for root, dirs, files in os.walk('template'):
    for file in files:
        if file.endswith(('.html', '.js', '.css')):
            patch_file(os.path.join(root, file))

for root, dirs, files in os.walk('static'):
    for file in files:
        if file.endswith(('.html', '.js', '.css')):
            patch_file(os.path.join(root, file))

print("UI patches applied.")
