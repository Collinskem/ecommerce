from django.urls import path, re_path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    re_path('add/(?P<product_id>\d+)/', views.cart_add, name='cart_add'),
    re_path('remove/(?P<product_id>\d+)/', views.cart_remove, name='cart_remove'),
]
