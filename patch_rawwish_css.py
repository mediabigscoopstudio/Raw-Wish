import re

with open('static/main/css/rawwish.css', 'r') as f:
    content = f.read()

content = content.replace(
    '''background: var(--rw-plum);
    color: #fff;
    border-color: var(--rw-plum);''',
    '''background: #421035 !important;
    color: #F4EADF !important;
    border-color: #421035 !important;'''
)

content = content.replace(
    '''.v-label-pill:hover { border-color: var(--rw-plum); }''',
    '''.v-label-pill:hover { border-color: #421035 !important; }'''
)

with open('static/main/css/rawwish.css', 'w') as f:
    f.write(content)
