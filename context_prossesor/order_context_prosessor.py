from order.models import Order


def order_context_prosessor(request):
    all_orders = Order.objects.all()
    context = {'all_orders': all_orders}
    return context
