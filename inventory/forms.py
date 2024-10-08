from django import forms
from . import models

class ProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields =['name','description','price','unit','stock_quantity', 'brand', 'category']


class BrandForm(forms.ModelForm):
    class Meta:
        model = models.Brand
        fields = ['name']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = ['name']

class UnitForm(forms.ModelForm):
    class Meta:
        model = models.Unit
        fields = ['name', 'shortname']