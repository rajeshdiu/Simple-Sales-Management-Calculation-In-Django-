
from django.contrib import admin
from django.urls import path
from myApp.views import *


urlpatterns = [
    path('', AddProductPage,name="AddProductPage"),
    path('productListPage/', productListPage,name="productListPage"),
    
]
