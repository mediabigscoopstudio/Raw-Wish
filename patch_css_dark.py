with open('static/main/css/rawwish.css', 'r') as f:
    content = f.read()

old_css = """/* Custom Newsletter Input */
.newsletter-instagram-section input:focus {
    box-shadow: none !important;
    outline: none !important;
    background: transparent !important;
    color: #231C18 !important;
}
.newsletter-instagram-section input::placeholder {
    color: rgba(35,28,24,0.5) !important;
}"""

new_css = """/* Custom Newsletter Input */
.newsletter-instagram-section input:focus {
    box-shadow: none !important;
    outline: none !important;
    background: transparent !important;
    color: #F8F6F0 !important;
}
.newsletter-instagram-section input::placeholder {
    color: rgba(248,246,240,0.5) !important;
}"""

content = content.replace(old_css, new_css)

with open('static/main/css/rawwish.css', 'w') as f:
    f.write(content)
