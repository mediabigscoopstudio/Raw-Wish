with open('template/main/base.html', 'r') as f:
    html = f.read()

import re

# Remove the individual css links
html = re.sub(r'<link rel="stylesheet" href="/static/main/css/base\.css\?v=\{%.*?%\}.*?">', '', html)
html = re.sub(r'<link rel="stylesheet" href="/static/main/css/rawwish\.css\?v=\{%.*?%\}.*?">', '', html)

# Inject minified css after bootstrap
bootstrap_icons = '<link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css" rel="stylesheet">'
html = html.replace(bootstrap_icons, bootstrap_icons + '\n  <link rel="stylesheet" href="/static/main/css/style.min.css?v={% now "U" %}">')

with open('template/main/base.html', 'w') as f:
    f.write(html)
