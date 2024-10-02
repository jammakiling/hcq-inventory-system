from django.db import models

# Create your models here.



class Brand(models.Model):
    name= models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):
    name= models.CharField(max_length=50)

    def __str__(self):
        return self.name




class Product(models.Model):
    name= models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    stock_quantity = models.PositiveIntegerField()
    

    brand = models.ForeignKey(
        Brand, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )
    
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )

    def __str__(self):
        return self.name
    