import re

with open('dash/views.py', 'r') as f:
    views_content = f.read()

new_index = """def index(request):
    time_filter = request.GET.get('time_filter', 'today')
    now = timezone.now()
    
    # Base querysets
    orders_qs = Order.objects.all().order_by('-created_at')
    customers_qs = Customers.objects.all()
    
    start_date = None
    end_date = None
    
    if time_filter == 'today':
        start_date = now.replace(hour=0, minute=0, second=0, microsecond=0)
    elif time_filter == 'yesterday':
        start_date = (now - timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
        end_date = start_date + timedelta(days=1)
    elif time_filter == 'this_week':
        start_date = now - timedelta(days=now.weekday())
        start_date = start_date.replace(hour=0, minute=0, second=0, microsecond=0)
    elif time_filter == 'this_month':
        start_date = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    elif time_filter == 'this_quarter':
        quarter_month = ((now.month - 1) // 3) * 3 + 1
        start_date = now.replace(month=quarter_month, day=1, hour=0, minute=0, second=0, microsecond=0)
    elif time_filter == 'this_fy':
        # Assuming FY starts in April
        fy_year = now.year if now.month >= 4 else now.year - 1
        start_date = now.replace(year=fy_year, month=4, day=1, hour=0, minute=0, second=0, microsecond=0)
    elif time_filter == 'this_year':
        start_date = now.replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
    else: # all_time
        pass

    filtered_orders = orders_qs
    filtered_customers = customers_qs
    
    if start_date:
        filtered_orders = filtered_orders.filter(created_at__gte=start_date)
        filtered_customers = filtered_customers.filter(user__date_joined__gte=start_date)
    if end_date:
        filtered_orders = filtered_orders.filter(created_at__lt=end_date)
        filtered_customers = filtered_customers.filter(user__date_joined__lt=end_date)
        
    # KPIs
    from django.db.models import Sum, Count, Q
    paid_orders = filtered_orders.filter(status__in=['Paid', 'Processing', 'Shipped', 'Out for Delivery', 'Delivered'])
    total_revenue = paid_orders.aggregate(Sum('total'))['total__sum'] or 0
    total_orders = filtered_orders.count()
    aov = (total_revenue / total_orders) if total_orders > 0 else 0
    new_customers = filtered_customers.count()
    
    # Support Health
    total_support = SupportQuery.objects.count()
    open_support = SupportQuery.objects.filter(status__in=['OPEN', 'ESCALATED', 'ACTION_REQUIRED']).count()
    resolved_today = SupportQuery.objects.filter(status='RESOLVED', resolved_at__gte=now.replace(hour=0, minute=0, second=0, microsecond=0)).count()

    # Kanban grouping - use filtered_orders so Kanban also obeys time filter, or show all? 
    # Usually Kanban should show active orders regardless of time filter, or time filter affects it?
    # Let's show active orders in Kanban from the filtered set to match the metrics.
    grouped_orders = {
        'pending': [],
        'processing': [],
        'shipped': [],
        'out_for_delivery': [],
        'delivered': [],
        'cancelled': [],
    }
    
    for order in filtered_orders:
        status_key = order.status.lower().replace(' ', '_')
        if status_key in grouped_orders:
            grouped_orders[status_key].append(order)
            
    context = {
        'time_filter': time_filter,
        'total_revenue': total_revenue,
        'total_orders': total_orders,
        'aov': aov,
        'new_customers': new_customers,
        
        # Support
        'open_support': open_support,
        'resolved_today': resolved_today,
        
        # Kanban
        'grouped_orders': grouped_orders,
        'all_orders': filtered_orders, # needed for template?
    }
    return render(request, 'dash/index.html', context)
"""

# Replace the index view
views_content = re.sub(r'def index\(request\):.*?return render\(request, \'dash/index\.html\', context\)', new_index, views_content, flags=re.DOTALL)

with open('dash/views.py', 'w') as f:
    f.write(views_content)
