with open('template/main/product_detail.html', 'r') as f:
    content = f.read()

# Replace variables
content = content.replace('var(--rawwish-cream)', 'var(--rw-cream)')
content = content.replace('var(--rawwish-charcoal)', 'var(--rw-ink)')
content = content.replace('var(--rawwish-brown)', 'var(--rw-muted)')
content = content.replace('var(--rawwish-rust)', 'var(--rw-plum)')
content = content.replace('var(--rawwish-dark)', 'var(--rw-plum-dark)')

# Replace typography classes if they exist
content = content.replace('font-family: var(--font-heading);', 'font-family: var(--font-serif);')
content = content.replace('font-family: var(--font-body);', 'font-family: var(--font-sans);')

# Make main image layout editorial (4:5 or similar rather than rounded box)
content = content.replace('border-radius: var(--radius-sm);', 'border-radius: 0;')
content = content.replace('border-radius: var(--radius-md);', 'border-radius: 0;')
content = content.replace('border-radius: var(--radius-lg);', 'border-radius: 0;')
content = content.replace('border-radius: var(--radius-pill);', 'border-radius: 0;')

with open('template/main/product_detail.html', 'w') as f:
    f.write(content)
