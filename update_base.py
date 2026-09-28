import re

with open('template/main/base.html', 'r') as f:
    content = f.read()

# Replace all SEO metadata block
seo_block_old = r'<title>.*?</title>.*?<meta name="description" content=".*?">.*?<meta name="keywords" content=".*?">'
seo_block_new = """<title>{% block 'title' %}Rawwish | The Look That Matters{% endblock 'title' %}</title>
  <meta name="description" content="{% block 'meta_description' %}Thoughtfully crafted beauty essentials with clean ingredients, real intention and a deeper respect for you and the planet.{% endblock 'meta_description' %}">
  <meta name="keywords" content="{% block 'meta_keywords' %}Rawwish, cosmetics, skincare, body care, beauty essentials, clean beauty{% endblock 'meta_keywords' %}">"""

content = re.sub(seo_block_old, seo_block_new, content, flags=re.DOTALL)

# Replace OG and Twitter
og_block_old = r'<!-- Open Graph / Facebook -->.*?<!-- Twitter -->.*?<meta property="twitter:image".*?>'
og_block_new = """<!-- Open Graph / Facebook -->
  <meta property="og:type" content="{% block 'og_type' %}website{% endblock 'og_type' %}">
  <meta property="og:url" content="{% block 'og_url' %}{{ request.build_absolute_uri }}{% endblock 'og_url' %}">
  <meta property="og:title" content="{% block 'og_title' %}Rawwish | The Look That Matters{% endblock 'og_title' %}">
  <meta property="og:description" content="{% block 'og_description' %}Thoughtfully crafted beauty essentials with clean ingredients, real intention and a deeper respect for you and the planet.{% endblock 'og_description' %}">
  <meta property="og:image" content="{% block 'og_image' %}{{ request.scheme }}://{{ request.get_host }}/static/main/logos/LogoMain.webp{% endblock 'og_image' %}">
  <meta property="og:site_name" content="Rawwish">

  <!-- Twitter -->
  <meta property="twitter:card" content="{% block 'twitter_card' %}summary_large_image{% endblock 'twitter_card' %}">
  <meta property="twitter:url" content="{% block 'twitter_url' %}{{ request.build_absolute_uri }}{% endblock 'twitter_url' %}">
  <meta property="twitter:title" content="{% block 'twitter_title' %}Rawwish | The Look That Matters{% endblock 'twitter_title' %}">
  <meta property="twitter:description" content="{% block 'twitter_description' %}Thoughtfully crafted beauty essentials with clean ingredients, real intention and a deeper respect for you and the planet.{% endblock 'twitter_description' %}">
  <meta property="twitter:image" content="{% block 'twitter_image' %}{{ request.scheme }}://{{ request.get_host }}/static/main/logos/LogoMain.webp{% endblock 'twitter_image' %}">"""

content = re.sub(og_block_old, og_block_new, content, flags=re.DOTALL)

# Replace structured data
schema_old = r'<script type="application/ld\+json">.*?</script>'
schema_new = """<script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "Rawwish",
    "url": "{{ request.scheme }}://{{ request.get_host }}/",
    "logo": "{{ request.scheme }}://{{ request.get_host }}/static/main/logos/LogoMain.webp",
    "description": "Premium editorial cosmetics and beauty essentials.",
    "sameAs": [
      "https://www.instagram.com/rawwish"
    ]
  }
  </script>"""

content = re.sub(schema_old, schema_new, content, flags=re.DOTALL)

# Write it back
with open('template/main/base.html', 'w') as f:
    f.write(content)
