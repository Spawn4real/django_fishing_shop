from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from mainapp.models import Product


# Create your views here.
from .models import Cart


def cart(request):
    context = {
        'cart': request.user.cart.all}
    return render(request, 'cartapp/cart.html', context=context)


def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)

    cart_product = request.user.products.filter(id=pk).first()

    if not cart_product:
        cart_product = Cart(user=request.user, product=product)

    cart_product.quantity += 1
    cart_product.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove_from_cart(request, pk):
    return render(request, 'cartapp/cart.html')

