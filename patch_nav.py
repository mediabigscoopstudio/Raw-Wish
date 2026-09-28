with open('template/main/components/header.html', 'r') as f:
    content = f.read()

# Desktop
old_desktop = """                <nav class="desktop-nav-links">
                    <a href="/shop">Shop</a>
                    <a href="/about">Ingredients</a>
                    <a href="/learn">Learn</a>
                    <a href="/about">Our Story</a>
                    <a href="/journal">Journal</a>
                </nav>"""
new_desktop = """                <nav class="desktop-nav-links">
                    <a href="/shop">Shop</a>
                    <a href="/ingredients">Ingredients</a>
                    <a href="/about">Our Story</a>
                    <a href="/content">Journal</a>
                </nav>"""
content = content.replace(old_desktop, new_desktop)

# Same for mobile nav, it's actually in base.html right now! 
# Let's check base.html for mobile-nav-links

with open('template/main/components/header.html', 'w') as f:
    f.write(content)
