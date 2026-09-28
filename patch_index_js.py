with open('template/dash/index.html', 'r') as f:
    content = f.read()

# Replace playPopSound and playSuccessSound logic
content = content.replace(
    "if (audioCtx.state === 'suspended') audioCtx.resume();",
    "if (localStorage.getItem('rawwish_sounds_enabled') === 'false') return;\n        if (audioCtx.state === 'suspended') audioCtx.resume();"
)

content = content.replace(
    "if (navigator.vibrate) {",
    "if (navigator.vibrate && localStorage.getItem('rawwish_haptics_enabled') !== 'false') {"
)

content = content.replace(
    "if (navigator.vibrate) navigator.vibrate([30, 50, 30]);",
    "if (navigator.vibrate && localStorage.getItem('rawwish_haptics_enabled') !== 'false') navigator.vibrate([30, 50, 30]);"
)

with open('template/dash/index.html', 'w') as f:
    f.write(content)
