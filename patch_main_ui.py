import os
import re

CSS_REPLACEMENTS = {
    'ROAST, BREW, ORIGINS': 'SHADES, ROUTINE, COLLECTIONS',
    'Coorg': 'Dermatology',
    'Chikmagalur': 'Paris',
    'Wayanad': 'Seoul',
    'Nilgiris': 'London',
    'UNDERSTANDING ROASTS': 'UNDERSTANDING SHADES',
    'BREW TECHNIQUES': 'APPLICATION TECHNIQUES',
    'LIGHT ROAST': 'SHEER COVERAGE',
    'MEDIUM ROAST': 'MEDIUM COVERAGE',
    'DARK ROAST': 'FULL COVERAGE',
    'COLD BREW': 'NIGHT ROUTINE',
    'French Press': 'Beauty Blender',
    'Filter Cosmetics': 'Skincare Sets',
    'South Indian Filter': 'Matte Finish',
    'Drip': 'Sponge',
    'Espresso': 'Liquid Foundation',
    'FRESHLY ROASTED & PACKED': 'CRUELTY FREE & VEGAN',
    'FRESHLY ROASTED': 'BEST SELLERS',
    'BREW BETTER': 'GLOW BETTER',
    'shadeing experience': 'formulation experience',
    'estate_coorg': 'lab_dermatology',
    'estate_chikmagalur': 'lab_paris',
    'estate_wayanad': 'lab_seoul',
    'estate_nilgiris': 'lab_london',
}

def patch_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = content
        for k, v in CSS_REPLACEMENTS.items():
            # case insensitive replacement for some
            new_content = re.sub(re.escape(k), v, new_content, flags=re.IGNORECASE)
            
        if content != new_content:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_content)
    except Exception as e:
        pass

for root, dirs, files in os.walk('template/main'):
    for file in files:
        if file.endswith(('.html', '.js', '.css')):
            patch_file(os.path.join(root, file))

print("Main UI patches applied.")
