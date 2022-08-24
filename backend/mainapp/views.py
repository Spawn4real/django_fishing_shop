from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import random

from .models import Product, ProductCategory
from cartapp.models import Cart

# Create your views here.


main_menu = [
    {'href': 'main', 'active_if': ['main'], 'name': 'Домой'},
    {'href': 'products:index', 'active_if': ['product:index', 'product:category'], 'name': 'Продукты'},
    {'href': 'contacts', 'active_if': ['contacts'], 'name': 'Контакты'},
]


def get_cart(user):
    if user.is_authenticated:
        return Cart.objects.filter(user=user)
    else:
        return []


def get_hot_product():
    products = Product.objects.filter(is_active=True, category__is_active=True)

    return random.sample(list(products), 1)[0]


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category, is_active=True).exclude(pk=hot_product.pk)[:3]

    return same_products


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
def products(request, pk=None, page=1):
    title = 'продукты'
    links_menu = ProductCategory.objects.filter(is_active=True)
    cart = get_cart(request.user)

    if pk is not None:
        if pk == 0:
            category = {
                'pk': 0,
                'name': 'все'
            }
            products = Product.objects.filter(is_active=True, category__is_active=True).order_by('price')

        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk, is_active=True, category__is_active=True).order_by('price')

        paginator = Paginator(products, 2)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)
        content = {
            'title': title,
            'links_menu': links_menu,
            'main_menu': main_menu,
            'category': category,
            'products': products_paginator,
            'cart': cart,
        }
        return render(request, 'mainapp/products_list.html', content)

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)
    products = Product.objects.all()

    content = {
        'title': title,
        'main_menu': main_menu,
        'products': products,
        'hot_product': hot_product,
        'same_products': same_products,
        'links_menu': links_menu,
        'cart': cart,
    }

    return render(request, 'mainapp/products.html', content)


def product(request, pk):
    title = 'продукты'
    links_menu = ProductCategory.objects.filter(is_active=True)

    product = get_object_or_404(Product, pk=pk)

    content = {
        'title': title,
        'main_menu': main_menu,
        'links_menu': links_menu,
        'product': product,
        'cart': get_cart(request.user),
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
