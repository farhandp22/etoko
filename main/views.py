from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306245743',
        'name': 'Farhan Dwi Putra',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)
