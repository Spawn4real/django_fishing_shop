from django.shortcuts import render, get_object_or_404
from .models import Product, ProductCategory

# Create your views here.

main_menu = [
    {'href': '/', 'name': 'Домой'},
    {'href': '/products', 'name': 'Продукты'},
    {'href': '/contacts', 'name': 'Контакты'},
]


# Контроллер для домашней странциы
def main(request):
    title = 'Главная'
    products = Product.objects.all()
    context = {
        'title': title,
        'main_menu': main_menu,
        'products': products,
    }
    return render(request, 'mainapp/main.html', context=context)


# Контроллер для страницы с товарами
def products(request, pk=None):
    if not pk:
        selected_category = ProductCategory.objects.first()
    else:
        selected_category = get_object_or_404(ProductCategory, id=pk)
    title = 'Каталог'
    categories = ProductCategory.objects.all()
    products = Product.objects.filter(categories=selected_category)
    context = {
        'title': title,
        'main_menu': main_menu,
        'selected_category': selected_category,
        'categories': categories,
        'products': products,
    }
    return render(request, 'mainapp/products.html', context=context)


# Контроллер для страницы с контактами
def contacts(request):
    title = 'Контакты'
    context = {
        'title': title,
        'main_menu': main_menu,
    }
    return render(request, 'mainapp/contacts.html', context=context)
