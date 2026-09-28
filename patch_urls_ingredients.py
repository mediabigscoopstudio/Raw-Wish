with open('main/urls.py', 'r') as f:
    content = f.read()

content = content.replace("path(\"about\", views.about, name='about'),",
                          "path(\"about/\", views.about, name='about'),\n    path(\"ingredients/\", views.ingredients, name='ingredients'),")
# The original code has `path("about", views.about, name='about'),`
# Let's replace exactly that

with open('main/urls.py', 'w') as f:
    f.write(content)
