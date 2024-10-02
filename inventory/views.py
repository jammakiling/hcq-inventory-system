from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .models import Product, Brand, Category
from .forms import ProductForm, BrandForm, CategoryForm

#Product
# View Product List
def product_list(request):
   products = Product.objects.all()
   return render(request, 'inventory/product_list.html' , {'products': products})

# Create a product
def product_create(request):
   if request.method == 'POST':
      form = ProductForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('inventory:product_list')
   else:
      form = ProductForm()
      return render (request, 'inventory/product_form.html' , {'form' :form})
   
# Update a product
def product_update(request, pk):
   product = get_object_or_404(Product, pk=pk)
   if request.method =='POST':
      form =ProductForm(request.POST, instance=product)
      if form.is_valid():
         form.save()
         return redirect('inventory:product_list')
   else:
      form = ProductForm(instance=product)
   return render(request, 'inventory/product_form.html', {'form': form})

# Delete a product
def product_delete(request, pk):
   product = get_object_or_404(Product, pk=pk)
   if request.method == 'POST':
      product.delete()
      return redirect('inventory:product_list')
   return render(request, 'inventory/product_confirm_delete.html', {'product':product})

#Brand
# View Brand List
def brand_list(request):
   brands = Brand.objects.all()
   return render(request, 'inventory/brand_list.html' , {'brands': brands})

# Create a brand
def brand_create(request):
   if request.method == 'POST':
      form = BrandForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('inventory:brand_list')
   else:
      form = BrandForm()
      return render (request, 'inventory/brand_form.html' , {'form' :form})
   
# Update a Brand
def brand_update(request, pk):
   brand = get_object_or_404(Brand, pk=pk)
   if request.method =='POST':
      form =BrandForm(request.POST, instance=brand)
      if form.is_valid():
         form.save()
         return redirect('inventory:brand_list')
   else:
      form = BrandForm(instance=brand)
   return render(request, 'inventory/brand_form.html', {'form': form})

# Delete a Brand
def brand_delete(request, pk):
   brand = get_object_or_404(Brand, pk=pk)
   if request.method == 'POST':
      brand.delete()
      return redirect('inventory:brand_list')
   return render(request, 'inventory/brand_confirm_delete.html', {'brand':brand})

#Category