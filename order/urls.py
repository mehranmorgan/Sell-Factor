from django.urls import path
from . import views

app_name = 'order'
urlpatterns = [
    path('Order_register', views.order_register, name='order_register'),
    path('Order_remove/<int:id>', views.order_remove, name='order_remove'),
    path('order_item/<int:id>', views.order_item, name='order_item'),
    path('add_item', views.add_item, name='add_item'),
    path('show_item_list/<int:id>', views.show_item_list, name='show_item_list'),
    path('delete_item_list/<int:order_id>/<int:product_id>', views.delete_item_list, name='delete_item_list'),
    path('factor/<int:id>', views.factor, name='factor'),
    path('show_item_list_no_price/<int:id>', views.show_item_list_no_price, name='show_item_list_no_price'),
    path('factor_no_price/<int:id>', views.factor_no_price, name='factor_no_price'),
]