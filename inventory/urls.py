from django.urls import path
from . import views


app_name = 'inventory'

urlpatterns = [
    path('products/', views.product_list ,name ='product_list'),
    path('products/create/', views.product_create, name='product_create'),
    path('products/update/<int:pk>/', views.product_update, name='product_update'),
    path('products/delete/<int:pk>/', views.product_delete, name='product_delete'),
    path('products/brands/', views.brand_list ,name ='brand_list'),
    path('brands/create/', views.brand_create, name='brand_create'),
    path('brands/update/<int:pk>/', views.brand_update, name='brand_update'),
    path('brands/delete/<int:pk>/', views.brand_delete, name='brand_delete'),

]