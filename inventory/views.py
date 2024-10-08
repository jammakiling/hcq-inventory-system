from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .models import Product, Brand, Category, Unit
from .forms import ProductForm, BrandForm, CategoryForm ,UnitForm

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
# View Category List
def category_list(request):
   categories = Category.objects.all()
   return render(request, 'inventory/category_list.html' , {'categories': categories})

# Create a category
def category_create(request):
   if request.method == 'POST':
      form= CategoryForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('inventory:category_list')
   else:
      form = CategoryForm()
      return render (request, 'inventory/category_form.html' , {'form' :form})
   
# Update a category
def category_update(request, pk):
   category = get_object_or_404(Category, pk=pk)
   if request.method =='POST':
      form =CategoryForm(request.POST, instance=category)
      if form.is_valid():
         form.save()
         return redirect('inventory:category_list')
   else:
      form = CategoryForm(instance=category)
   return render(request, 'inventory/category_form.html', {'form': form})

# Delete a category
def category_delete(request, pk):
   category = get_object_or_404(Category, pk=pk)
   if request.method == 'POST':
      category.delete()
      return redirect('inventory:category_list')
   return render(request, 'inventory/category_confirm_delete.html', {'category':category})

#Unit
# View Unit List
def unit_list(request):
   units = Unit.objects.all()
   return render(request, 'inventory/unit_list.html' , {'units': units})

# Create a unit
def unit_create(request):
   if request.method == 'POST':
      form= UnitForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('inventory:unit_list')
   else:
      form = UnitForm()
      return render (request, 'inventory/unit_form.html' , {'form' :form})
   
# Update a unit
def unit_update(request, pk):
   unit = get_object_or_404(Unit, pk=pk)
   if request.method =='POST':
      form =UnitForm(request.POST, instance=unit)
      if form.is_valid():
         form.save()
         return redirect('inventory:unit_list')
   else:
      form = UnitForm(instance=unit)
   return render(request, 'inventory/unit_form.html', {'form': form})

# Delete a unit
def unit_delete(request, pk):
   unit = get_object_or_404(Unit, pk=pk)
   if request.method == 'POST':
      unit.delete()
      return redirect('inventory:unit_list')
   return render(request, 'inventory/unit_confirm_delete.html', {'unit':unit})
