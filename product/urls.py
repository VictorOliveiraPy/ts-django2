from django.urls import path

from . import views

app_name = 'product'


urlpatterns = [
    path('', views.home, name='home'),
    path('product', views.product, name='product'),
    path('create/product', views.create_product, name='product-create')
]
