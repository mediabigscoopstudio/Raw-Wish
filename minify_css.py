import re

def minify(css):
    # Remove comments
    css = re.sub(r'/\*[\s\S]*?\*/', '', css)
    # Remove newlines and tabs
    css = re.sub(r'\s+', ' ', css)
    # Remove spaces around tokens
    css = re.sub(r'\s*([\{\}\:\;\,\>])\s*', r'\1', css)
    # Remove trailing semicolons
    css = re.sub(r';}', '}', css)
    return css.strip()

with open('static/main/css/base.css', 'r') as f:
    base = f.read()

with open('static/main/css/rawwish.css', 'r') as f:
    rawwish = f.read()

minified = minify(base + "\n" + rawwish)

with open('static/main/css/style.min.css', 'w') as f:
    f.write(minified)

# Update base.html
with open('template/main/base.html', 'r') as f:
    html = f.read()

# Replace fonts
html = re.sub(
    r'<link href="https://fonts\.googleapis\.com/css2\?family=Merriweather.*?rel="stylesheet">',
    '', html, flags=re.DOTALL
)
html = re.sub(
    r'<link href="https://fonts\.googleapis\.com/css2\?family=Playfair\+Display.*?rel="stylesheet">',
    '<link href="https://fonts.googleapis.com/css2?family=Merriweather:ital,wght@0,400;0,700;0,900;1,400;1,700&family=Montserrat:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">',
    html, flags=re.DOTALL
)

# Replace css links
css_links = r'<link rel="stylesheet" href="/static/main/css/base.css\?v=.*?">\s*<link rel="stylesheet" href="/static/main/css/base.css\?v=.*?">\s*<link rel="stylesheet" href="/static/main/css/rawwish.css\?v=.*?">'
html = re.sub(css_links, '<link rel="stylesheet" href="/static/main/css/style.min.css?v={% now "U" %}">', html, flags=re.DOTALL)

with open('template/main/base.html', 'w') as f:
    f.write(html)
