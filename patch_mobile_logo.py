with open('template/main/components/header.html', 'r') as f:
    content = f.read()

# Replace mobile logo with vector.webp
old_mobile = """            <a href="/" class="header-logo">
                <img src="/static/main/logos/Logo.webp" alt="Raw Wish" style="height: 60px; object-fit: contain;">
            </a>"""

new_mobile = """            <a href="/" class="header-logo">
                <img src="/static/main/logos/vector.webp" alt="Rawwish Icon" style="height: 45px; object-fit: contain;">
            </a>"""

content = content.replace(old_mobile, new_mobile)

with open('template/main/components/header.html', 'w') as f:
    f.write(content)
