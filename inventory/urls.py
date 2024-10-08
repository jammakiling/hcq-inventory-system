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
    path('products/categories/', views.category_list ,name ='category_list'),
    path('categories/create/', views.category_create, name='category_create'),
    path('categories/update/<int:pk>/', views.category_update, name='category_update'),
    path('categories/delete/<int:pk>/', views.category_delete, name='category_delete'),
    path('products/units/', views.unit_list ,name ='unit_list'),
    path('units/create/', views.unit_create, name='unit_create'),
    path('units/update/<int:pk>/', views.unit_update, name='unit_update'),
    path('units/delete/<int:pk>/', views.unit_delete, name='unit_delete'),

]