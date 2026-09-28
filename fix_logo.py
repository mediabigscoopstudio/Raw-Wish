with open('template/main/base.html', 'r') as f:
    content = f.read()

# The header logo is probably inside the header block
content = content.replace('<img src="/static/main/images/og-rawwish.webp" alt="Raw Wish" height="60">', '<img src="/static/main/logos/Logo.webp" alt="Raw Wish" height="60">')

with open('template/main/base.html', 'w') as f:
    f.write(content)
