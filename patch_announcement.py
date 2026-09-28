with open('template/main/components/announcement.html', 'r') as f:
    content = f.read()

content = content.replace('var(--rawwish-dark)', 'var(--rw-plum-dark)')
content = content.replace('var(--rawwish-gold)', 'var(--rw-dusty-rose)')
content = content.replace('SOURCED FROM INDIAN PLANTATIONS', 'PURE & CLEAN INGREDIENTS')
content = content.replace('ARTISANAL ROASTS', 'THOUGHTFUL FORMULATIONS')
content = content.replace('FRESHLY ROASTED WEEKLY', 'DERMATOLOGICALLY TESTED')
content = content.replace('100% SINGLE ORIGIN', 'CRUELTY FREE')

with open('template/main/components/announcement.html', 'w') as f:
    f.write(content)
