with open('template/main/base.html', 'r') as f:
    content = f.read()

old_mobile = """    <nav class="mobile-nav-links d-flex flex-column gap-3">
        <a href="/shop">Shop</a>
        <a href="/origins">Origins</a>
        <a href="/learn">Learn</a>
        <a href="/about">Our Story</a>
        <a href="/journal">Journal</a>
        
    </nav>"""
new_mobile = """    <nav class="mobile-nav-links d-flex flex-column gap-3">
        <a href="/shop">Shop</a>
        <a href="/ingredients">Ingredients</a>
        <a href="/about">Our Story</a>
        <a href="/content">Journal</a>
    </nav>"""
content = content.replace(old_mobile, new_mobile)

with open('template/main/base.html', 'w') as f:
    f.write(content)
