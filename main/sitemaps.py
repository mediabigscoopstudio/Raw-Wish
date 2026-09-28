from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from dash.models import Product

class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return ['index', 'about', 'ingredients', 'shop']

    def location(self, item):
        return reverse(item)

class ProductSitemap(Sitemap):
    priority = 0.9
    changefreq = 'daily'

    def items(self):
        return Product.objects.all()

    def location(self, item):
        category_slug = item.category.slug if item.category else 'all'
        sub_category_slug = item.sub_category.slug if item.sub_category else 'all'
        return reverse('product_detail', kwargs={
            'category_slug': category_slug,
            'subcategory_slug': sub_category_slug,
            'product_slug': item.slug
        })
