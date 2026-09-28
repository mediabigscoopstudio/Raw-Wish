import re

with open('rawwish/settings.py', 'r') as f:
    content = f.read()

content = content.replace('"django.contrib.staticfiles",', '"django.contrib.staticfiles",\n    "django.contrib.sitemaps",\n    "django.contrib.sites",')

if "SITE_ID =" not in content:
    content += "\nSITE_ID = 1\n"

with open('rawwish/settings.py', 'w') as f:
    f.write(content)
