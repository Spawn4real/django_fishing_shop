from django.shortcuts import render

# Create your views here.

# Контроллер для домашней странциы
def home(request):
    return render(request, 'mainapp/home.html')

# Контроллер для страницы с товарами
def products(request):
    return render(request, 'mainapp/products.html')

# Контроллер для страницы с контактами
def contacts(request):
    return render(request, 'mainapp/contacts.html')
