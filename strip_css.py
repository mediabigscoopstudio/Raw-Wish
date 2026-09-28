with open('template/main/shop.html', 'r') as f:
    content = f.read()

start_idx = content.find('  /* Premium Card Styles')
end_idx = content.find('/* Horizontal Layout specific */', start_idx)

if start_idx != -1 and end_idx != -1:
    old_css = content[start_idx:end_idx]
    content = content.replace(old_css, "")

with open('template/main/shop.html', 'w') as f:
    f.write(content)
