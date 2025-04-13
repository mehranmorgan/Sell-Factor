from django.urls import path
from . import views

app_name = 'product'
urlpatterns = [
    path('', views.show_product, name='show_product'),
    path('add_product', views.add_product, name='add_product'),
    path('delete_product/<int:id>', views.delete_product, name='delete_product'),
]