with open('template/main/components/newsletter.html', 'r') as f:
    content = f.read()

content = content.replace('Get updates on new harvests, routineing tips, exclusive offers and stories from our plantations.', 'Join our community for early access to new launches, skincare advice, and exclusive offers.')
content = content.replace('var(--rawwish-rust)', 'var(--rw-plum)')
content = content.replace('var(--rawwish-cream)', 'var(--rw-cream)')

with open('template/main/components/newsletter.html', 'w') as f:
    f.write(content)
