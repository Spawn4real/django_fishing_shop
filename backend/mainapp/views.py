from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Product, ProductCategory

# Create your views here.


main_menu = [
    {'href': 'main', 'active_if': ['main'], 'name': 'Домой'},
    {'href': 'products:index', 'active_if': ['product:index', 'product:category'], 'name': 'Продукты'},
    {'href': 'contacts', 'active_if': ['contacts'], 'name': 'Контакты'},
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
def products(request, pk=0):
    if not pk:
        selected_category = None
        selected_category_dict = {'name': 'Всё', 'href': reverse('products:index', args=[])}
    else:
        selected_category = get_object_or_404(ProductCategory, id=pk)
        selected_category_dict = {'name': selected_category.name, 'href': reverse('products:category',
                                                                                  args=[selected_category.id])}

    title = 'Каталог'
    categories = [{'name': c.name, 'href': reverse('products:category', args=[c.id])}
                  for c in ProductCategory.objects.all()]
    categories = [{'name': 'Всё', 'href': reverse('products:index')}, *categories]
    if selected_category:
        products_query = Product.objects.filter(category=selected_category)
    else:
        products_query = Product.objects.all()

    hot_product = Product.objects.hot_product

    products = products_query.order_by('price')

    context = {
        'title': title,
        'main_menu': main_menu,
        'selected_category': selected_category_dict,
        'categories': categories,
        'products': products,
        'hot_product': hot_product,
    }
    return render(request, 'mainapp/products.html', context=context)


def product(request, pk):
    title = 'продукты'
    content = {
        'title': title,
        'links_menu': ProductCategory.objects.all(),
        'product': get_object_or_404(Product, pk=pk),
        'cart': get_object_or_404(request.user),
    }
    return render(request, 'mainapp/product.html', content)


# Контроллер для страницы с контактами
def contacts(request):
    title = 'Контакты'

    context = {
        'title': title,
        'main_menu': main_menu,
    }
    return render(request, 'mainapp/contacts.html', context=context)
