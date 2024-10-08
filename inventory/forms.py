from django import forms
from . import models
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields =['product_code','name','description','price','unit','stock_quantity', 'brand', 'category']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        # Add Bootstrap class to each field
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


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