from dash.models import Product

products = Product.objects.all()
for p in products:
    print(p.name)
