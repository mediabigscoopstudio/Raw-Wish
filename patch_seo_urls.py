import re

with open('main/urls.py', 'r') as f:
    content = f.read()

# Add sitemaps import
if 'from django.contrib.sitemaps.views import sitemap' not in content:
    content = content.replace("from django.urls import path", "from django.urls import path\nfrom django.contrib.sitemaps.views import sitemap\nfrom main.sitemaps import ProductSitemap, StaticViewSitemap")

# Add sitemaps config
sitemap_config = """
sitemaps = {
    'static': StaticViewSitemap,
    'products': ProductSitemap,
}
"""

if 'sitemaps = {' not in content:
    content = content.replace("urlpatterns = [", sitemap_config + "\nurlpatterns = [")

# Add url routes
new_routes = """
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('llms.txt', TemplateView.as_view(template_name='llms.txt', content_type='text/plain')),
"""

content = content.replace("path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),", "path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),\n" + new_routes)

with open('main/urls.py', 'w') as f:
    f.write(content)
