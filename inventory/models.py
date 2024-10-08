from django.db import models
import uuid

# Create your models here.



class Brand(models.Model):
    name= models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):
    name= models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Unit(models.Model):
    name= models.CharField(max_length=20)
    shortname= models.CharField(max_length=3)

    def __str__(self):
        return self.name



class Product(models.Model):
    product_code = models.CharField(max_length=50, unique=True)
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

    unit = models.ForeignKey(
        Unit, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )


    def save(self, *args, **kwargs):
        if not self.product_code:  # If no product code is set
            self.product_code = str(uuid.uuid4())  # Generate a new UUID for product code
        super().save(*args, **kwargs)
    def __str__(self):
        f'{self.name} ({self.product_code})'
    