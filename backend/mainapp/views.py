from django.shortcuts import render

# Create your views here.

main_menu = [
    {'href': '/', 'name': 'Домой'},
    {'href': '/products', 'name': 'Продукты'},
    {'href': '/contacts', 'name': 'Контакты'},
]

links_menu = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'hre f': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
]


# Контроллер для домашней странциы
def main(request):
    title = 'Главная'
    context = {
        'title': title,
        'main_menu': main_menu,
    }
    return render(request, 'mainapp/main.html', context=context)


# Контроллер для страницы с товарами
def products(request):
    title = 'Каталог'
    context = {
        'title': title,
        'main_menu':main_menu,
        'links_menu': links_menu,
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
