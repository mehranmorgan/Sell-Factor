from django.urls import path
from . import views



app_name = 'account'
urlpatterns = [
    path('register',views.user_register,name='register'),
    path('logout',views.user_logout,name='logout'),
    path('login',views.user_login,name='login'),
]