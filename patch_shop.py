with open('template/main/shop.html', 'r') as f:
    content = f.read()

# Fix SEO metadata
content = content.replace('{% if category %}{{ category.title }} | Shop{% else %}Shop All Cosmetics{% endif %} - Raw Wish', '{% if category %}{{ category.title }}{% else %}Shop All Essentials{% endif %} - Rawwish')
content = content.replace('Explore our authentic collection of South Indian Skincare Sets. Estate-grown, artisanal shades shipped fresh.', 'Discover our collection of thoughtfully crafted beauty essentials and skincare routines.')

# Fix CSS styling by replacing the old .rawwish-card block
old_card_style_start = content.find('.rawwish-card {')
old_card_style_end = content.find('.card-details {')

if old_card_style_start != -1 and old_card_style_end != -1:
    new_card_style = """/* Premium Card Styles (Rawwish Editorial) */
  .rawwish-card {
    background: transparent;
    overflow: hidden;
    font-family: var(--font-sans);
    display: flex;
    flex-direction: column;
    border: none;
    transition: opacity 0.3s ease;
  }
  .rawwish-card:hover {
    opacity: 0.95;
  }

  .rawwish-card-img-wrap {
    position: relative;
    padding-top: 125%; /* 4:5 Aspect Ratio */
    background: var(--rw-cream);
    display: block;
    overflow: hidden;
  }
  .rawwish-card-img-wrap img {
    position: absolute;
    top: 0; left: 0;
    width: 100%; height: 100%;
    object-fit: cover;
    transition: transform 0.6s ease;
  }
  .rawwish-card:hover .rawwish-card-img-wrap img {
    transform: scale(1.03);
  }

  .badge-top-left {
    position: absolute;
    top: 10px; left: 10px;
    background: var(--rw-white);
    color: var(--rw-plum);
    padding: 4px 10px;
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 0.05em;
    text-transform: uppercase;
  }
  
  """
    content = content[:old_card_style_start] + new_card_style + content[old_card_style_end:]

# Fix typography inside cards
content = content.replace('color: var(--rawwish-charcoal);', 'color: var(--rw-ink);')
content = content.replace('color: var(--rawwish-brown);', 'color: var(--rw-muted);')
content = content.replace('color: var(--rawwish-rust);', 'color: var(--rw-plum);')
content = content.replace('var(--rawwish-cream)', 'var(--rw-cream)')

with open('template/main/shop.html', 'w') as f:
    f.write(content)
