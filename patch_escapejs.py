with open('template/main/base.html', 'r') as f:
    content = f.read()

content = content.replace("const clientId = '{{ GOOGLE_CLIENT_ID|escapejs }}';", "const clientId = '{{ GOOGLE_CLIENT_ID }}';")

with open('template/main/base.html', 'w') as f:
    f.write(content)
