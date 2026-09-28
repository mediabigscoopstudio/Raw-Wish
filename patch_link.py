with open('template/main/base.html', 'r') as f:
    content = f.read()

bad_string = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400<link rel="stylesheet" href="/static/main/css/base.css?v={% now "U" %}">family=Inter:wght@300;400;500;600<link rel="stylesheet" href="/static/main/css/base.css?v={% now "U" %}">display=swap" rel="stylesheet">'
good_string = '<link rel="stylesheet" href="/static/main/css/base.css?v={% now "U" %}">\n  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">'

content = content.replace(bad_string, good_string)

with open('template/main/base.html', 'w') as f:
    f.write(content)
