with open('template/main/components/header.html', 'r') as f:
    content = f.read()

content = content.replace('<a href="/origins">Origins</a>', '<a href="/about">Ingredients</a>')
content = content.replace('placeholder="Search cosmetics, equipment..."', 'placeholder="Search beauty essentials..."')

with open('template/main/components/header.html', 'w') as f:
    f.write(content)
