import re

with open('static/main/css/base.css', 'r') as f:
    content = f.read()

content = re.sub(r'\.cart-badge\s*\{[^}]*\}', 
                 '.cart-badge{position:absolute;top:-5px;right:-8px;background-color:#421035;color:#F4EADF;font-size:0.65rem;font-weight:bold;border-radius:50%;width:18px;height:18px;display:flex;align-items:center;justify-content:center;}', 
                 content)

with open('static/main/css/base.css', 'w') as f:
    f.write(content)
