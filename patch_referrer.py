with open('rawwish/settings.py', 'r') as f:
    content = f.read()

if 'SECURE_REFERRER_POLICY' in content:
    import re
    content = re.sub(r'SECURE_REFERRER_POLICY\s*=.*', "SECURE_REFERRER_POLICY = 'strict-origin-when-cross-origin'", content)
else:
    content += "\nSECURE_REFERRER_POLICY = 'strict-origin-when-cross-origin'\n"

with open('rawwish/settings.py', 'w') as f:
    f.write(content)
