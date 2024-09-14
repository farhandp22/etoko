from django.shortcuts import render, redirect
from main.forms import ProductForm
from main.models import Product

def show_main(request):
    data = Product.objects.all()
    context = {
        'npm' : '2306245743',
        'name': 'Farhan Dwi Putra',
        'class': 'PBP D', 
        'data' : data
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)