with open('rawwish/settings.py', 'r') as f:
    content = f.read()

content = content.replace("GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')", "GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID', '').strip()")
content = content.replace("GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')", "GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET', '').strip()")

with open('rawwish/settings.py', 'w') as f:
    f.write(content)
