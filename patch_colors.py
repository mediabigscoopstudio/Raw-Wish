import re

# UPDATE ABOUT.HTML
with open('template/main/about.html', 'r') as f:
    about = f.read()

# "Beauty without compromise" is currently inheriting color or doesn't have an explicit color.
# The section has `color: #FFFFFF;` but maybe there is a generic h1 style overriding it. 
# Let's explicitly set color: #FFFFFF.
about = about.replace(
    'h1 style="font-family: var(--font-serif); font-size: clamp(3.5rem, 6vw, 6rem); line-height: 1; letter-spacing: -0.02em; margin-bottom: 30px;"',
    'h1 style="font-family: var(--font-serif); font-size: clamp(3.5rem, 6vw, 6rem); line-height: 1; letter-spacing: -0.02em; margin-bottom: 30px; color: #FFFFFF;"'
)

# "What we stand for."
about = about.replace(
    'h2 style="font-family: var(--font-serif); font-size: clamp(2.5rem, 4vw, 3.5rem); line-height: 1.1; letter-spacing: -0.02em;"',
    'h2 style="font-family: var(--font-serif); font-size: clamp(2.5rem, 4vw, 3.5rem); line-height: 1.1; letter-spacing: -0.02em; color: #FFFFFF;"'
)

# "Pure Ingredients", "High Performance", "Conscious Creation"
about = about.replace(
    'h4 style="font-family: var(--font-serif); font-size: 1.5rem; margin-bottom: 15px;"',
    'h4 style="font-family: var(--font-serif); font-size: 1.5rem; margin-bottom: 15px; color: #FFFFFF;"'
)

with open('template/main/about.html', 'w') as f:
    f.write(about)


# UPDATE INGREDIENTS.HTML
with open('template/main/ingredients.html', 'r') as f:
    ing = f.read()

# "Powered by nature. Proven by science."
ing = ing.replace(
    'h1 style="font-family: var(--font-serif); font-size: clamp(3rem, 5vw, 5rem); line-height: 1; letter-spacing: -0.02em; margin-bottom: 30px;"',
    'h1 style="font-family: var(--font-serif); font-size: clamp(3rem, 5vw, 5rem); line-height: 1; letter-spacing: -0.02em; margin-bottom: 30px; color: #FFFFFF;"'
)

# "The Rawwish Standard"
ing = ing.replace(
    'h3 style="font-family: var(--font-serif); font-size: 2rem; margin-bottom: 20px;"',
    'h3 style="font-family: var(--font-serif); font-size: 2rem; margin-bottom: 20px; color: #FFFFFF;"'
)

with open('template/main/ingredients.html', 'w') as f:
    f.write(ing)
