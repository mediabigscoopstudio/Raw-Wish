import re

with open('template/dash/base.html', 'r') as f:
    content = f.read()

new_logo_html = """    <div class="logo-box">
        <a href="/" class="logo logo-light">
            <span class="logo-sm">
                <img src="/static/dash/assets/Logos/LogoDark.webp" alt="" height="70">
            </span>
            <span class="logo-lg">
                <img src="/static/dash/assets/Logos/LogoDark.webp" alt="" height="70">
            </span>
        </a>
        <a href="/" class="logo logo-dark">
            <span class="logo-sm">
                <img src="/static/dash/assets/Logos/LogoMain.webp" alt="" height="70">
            </span>
            <span class="logo-lg">
                <img src="/static/dash/assets/Logos/LogoMain.webp" alt="" height="70">
            </span>
        </a>
    </div>"""

content = re.sub(r'<div class="logo-box">.*?</div>', new_logo_html, content, flags=re.DOTALL)

with open('template/dash/base.html', 'w') as f:
    f.write(content)

print("Logo HTML restored in base.html")
