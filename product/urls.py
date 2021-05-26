from django.urls import path

from . import views

app_name = 'product'


urlpatterns = [
    path('', views.home, name='home'),
    path('product', views.product, name='product'),
    path('category', views.category, name='category'),
    path('create/product', views.create_product, name='product-create'),
    path('create/category', views.create_category, name='category-create')

]
