from django.shortcuts import render,redirect
from myApp.models import *

def AddProductPage(request):
    
    if request.method=="POST":
        
        total_price = 0
        
        product_name = request.POST.get("product_name")
        category =  request.POST.get("category")
        unit_price = float(request.POST.get("unit_price"))
        quantity =int(request.POST.get("quantity"))
        discount_percent = float(request.POST.get("discount_percent"))
        tax_percent = float(request.POST.get("tax_percent") )  
        
        print(product_name,category,unit_price,quantity,discount_percent,tax_percent)
        
        if unit_price:
        
            total_price = (unit_price*quantity) - ((unit_price * quantity)*discount_percent/100)+ ((unit_price * quantity)*tax_percent/100)
            
            data=ProductModel(
                product_name =product_name,
                category = category,
                unit_price = unit_price,
                quantity = quantity,
                discount_percent = discount_percent,
                tax_percent = tax_percent,
                total_price = total_price
            )
            data.save()
        return redirect("productListPage")
    return render(request,"AddProduct.html")


def productListPage(request):
    
    context={
        'products':ProductModel.objects.all()
    }
    
    return render(request,"productListPage.html",context)