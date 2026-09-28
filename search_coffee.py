import os
import re

terms = ["Kapi", "coffee", "KT-", "Coorg", "Chikmagalur", "Wayanad", "Araku", "Nilgiris", 
         "French Press", "Coffee Filter", "Coffee Beans", "Roast", "Dark Roast", "Medium Roast", "Light Roast", "Decaf"]
pattern = re.compile(r'\b(' + '|'.join(terms) + r')\b', re.IGNORECASE)

EXCLUDE_DIRS = {'.git', 'venv', 'libs', '.product_seed_cache', '.content_fill_image_cache', '.old_patch_scripts', 'media', 'node_modules', '__pycache__', 'graphify-out'}

def search_directory(directory):
    for root, dirs, files in os.walk(directory, topdown=True):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for name in files:
            if name.endswith(('.png', '.jpg', '.jpeg', '.gif', '.svg', '.woff', '.woff2', '.ttf', '.eot', '.pyc', '.json', '.sqlite3')): 
                continue
            file_path = os.path.join(root, name)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    for i, line in enumerate(f):
                        if pattern.search(line):
                            print(f"{file_path}:{i+1}: {line.strip()[:100]}")
            except UnicodeDecodeError:
                pass

search_directory(".")
