with open('template/main/shop.html', 'r') as f:
    content = f.read()

import re

# Find the start and end of .rawwish-card loop
start_idx = content.find('<div class="rawwish-card">')
end_idx = content.find('</div>\n      {% endfor %}', start_idx)

if start_idx != -1 and end_idx != -1:
    old_card = content[start_idx:end_idx + 6]
    content = content.replace(old_card, "{% include 'main/components/product_card.html' with product=p %}")

with open('template/main/shop.html', 'w') as f:
    f.write(content)
