import re

# Read dash/urls.py
with open('dash/urls.py', 'r') as f:
    urls_content = f.read()

if 'path("orders_kanban"' not in urls_content:
    urls_content = urls_content.replace(
        'path("",views.index,name=\'index\'),',
        'path("",views.index,name=\'index\'),\n    path("orders_kanban",views.orders_kanban,name=\'orders_kanban\'),'
    )
    with open('dash/urls.py', 'w') as f:
        f.write(urls_content)

# Read dash/views.py
with open('dash/views.py', 'r') as f:
    views_content = f.read()

# Duplicate index to orders_kanban
if 'def orders_kanban(request):' not in views_content:
    # Find the index function block
    index_match = re.search(r'def index\(request\):.*?(?=\ndef |\Z)', views_content, re.DOTALL)
    if index_match:
        index_code = index_match.group(0)
        # Rename the duplicated function to orders_kanban
        orders_kanban_code = index_code.replace('def index(request):', 'def orders_kanban(request):', 1)
        # Change the template returned by orders_kanban if it is index.html
        orders_kanban_code = orders_kanban_code.replace("render(request, 'dash/index.html'", "render(request, 'dash/orders_kanban.html'")
        
        # Now replace the original index function with the new command center logic
        new_index = """def index(request):
    time_filter = request.GET.get('time_filter', 'today')
    now = timezone.now()
    
    # Base querysets
    orders_qs = Order.objects.all()
    customers_qs = Customers.objects.all()
    
    if time_filter == 'today':
        start_date = now.replace(hour=0, minute=0, second=0, microsecond=0)
    elif time_filter == 'yesterday':
        start_date = (now - timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
        end_date = start_date + timedelta(days=1)
        orders_qs = orders_qs.filter(created_at__lt=end_date)
        customers_qs = customers_qs.filter(created_at__lt=end_date)
    elif time_filter == 'last_7_days':
        start_date = now - timedelta(days=7)
    elif time_filter == 'last_30_days':
        start_date = now - timedelta(days=30)
    elif time_filter == 'this_month':
        start_date = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    elif time_filter == 'this_year':
        start_date = now.replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
    else: # all_time
        start_date = None

    if start_date:
        orders_qs = orders_qs.filter(created_at__gte=start_date)
        customers_qs = customers_qs.filter(created_at__gte=start_date)
        
    # KPIs
    from django.db.models import Sum, Count, Q
    paid_orders = orders_qs.filter(status__in=['Paid', 'Processing', 'Shipped', 'Out for Delivery', 'Delivered'])
    total_revenue = paid_orders.aggregate(Sum('total'))['total__sum'] or 0
    total_orders = orders_qs.count()
    aov = (total_revenue / total_orders) if total_orders > 0 else 0
    new_customers = customers_qs.count()
    
    # Inventory Health
    low_stock = Variant.objects.filter(quantity__lt=10, quantity__gt=0).count()
    out_of_stock = Variant.objects.filter(quantity=0).count()
    total_products = Product.objects.count()
    total_variants = Variant.objects.count()
    
    pending_orders = orders_qs.filter(status='Pending').count()
    
    context = {
        'time_filter': time_filter,
        'total_revenue': total_revenue,
        'total_orders': total_orders,
        'aov': aov,
        'new_customers': new_customers,
        'low_stock': low_stock,
        'out_of_stock': out_of_stock,
        'pending_orders': pending_orders,
        'total_products': total_products,
        'total_variants': total_variants,
    }
    return render(request, 'dash/index.html', context)
"""
        views_content = views_content.replace(index_code, new_index + "\n\n" + orders_kanban_code)
        with open('dash/views.py', 'w') as f:
            f.write(views_content)
        print("Updated dash/views.py")

