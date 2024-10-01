from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .models import Product
from .forms import ProductForm


# Create your views here.
def product_list(request):
   products = Product.objects.all()
   return render(request, 'inventory/product_list.html' , {'products': products})

def product_create(request):
   if request.method == 'POST':
      form = ProductForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('inventory:product_list')
   else:
      form = ProductForm()
      return render (request, 'inventory/product_form.html' , {'form' :form})
   
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

def product_delete(request, pk):
   product = get_object_or_404(Product, pk=pk)
   if request.method == 'POST':
      product.delete()
      return redirect('inventory:product_list')
   return render(request, 'inventory/product_confirm_delete.html', {'product':product})