from django.shortcuts import render
from .models import Product

def show_main(request):
    data = Product.objects.all()
    context = {
        'npm' : '2306245743',
        'name': 'Farhan Dwi Putra',
        'class': 'PBP D', 
        'data' : data
    }

    return render(request, "main.html", context)
