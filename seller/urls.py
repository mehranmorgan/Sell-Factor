from django.urls import include, path
from . import views




app_name = 'seller'
urlpatterns = [
    path('',views.seller_list,name='seller-list' ),
    path('add_new_sellerr', views.add_new_seller, name='add_new_seller'),
    path('delete_seller/<int:pk>', views.delete_seller, name='delete_seller'),
]