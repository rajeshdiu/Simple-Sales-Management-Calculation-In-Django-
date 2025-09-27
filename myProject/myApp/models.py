from django.db import models


class CategoryModel(models.Model):
    
    categoryName=models.CharField(max_length=200) 
    
    def __str__(self):
        return self.categoryName

class ProductModel(models.Model):
    
    product_name = models.CharField(max_length=200,null=True) 
    category = models.CharField(max_length=100,null=True) 
    unit_price = models.DecimalField(max_digits=10, decimal_places=2,null=True) 
    quantity =models.PositiveIntegerField(null=True) 
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2, default=0,null=True) 
    tax_percent = models.DecimalField(max_digits=5, decimal_places=2, default=0,null=True) 
    total_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True) 
    sale_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.product_name+"-"+self.category