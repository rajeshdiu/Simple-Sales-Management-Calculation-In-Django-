from django.shortcuts import render,redirect
from myApp.models import *

def AddProductPage(request):
    
    
    
    if request.method=="POST":
        
        total_price = 0
        
        product_name = request.POST.get("product_name")
        category_id =  request.POST.get("category_id")
        unit_price = float(request.POST.get("unit_price"))
        quantity =int(request.POST.get("quantity"))
        discount_percent = float(request.POST.get("discount_percent"))
        tax_percent = float(request.POST.get("tax_percent") )  
        
        category_substance = CategoryModel.objects.get(id=category_id)
        
        if unit_price:
        
            total_price = (unit_price*quantity) - ((unit_price * quantity)*discount_percent/100)+ ((unit_price * quantity)*tax_percent/100)
            
            data=ProductModel(
                product_name =product_name,
                category = category_substance,
                unit_price = unit_price,
                quantity = quantity,
                discount_percent = discount_percent,
                tax_percent = tax_percent,
                total_price = total_price
            )
            data.save()
            
            return redirect("productListPage")
         
    categories = CategoryModel.objects.all() 
          
    context = {
            'categories':categories
        }
    return render(request,"AddProduct.html",context)


def productListPage(request):
    
    context={
        'products':ProductModel.objects.all()
    }
    
    return render(request,"productListPage.html",context)