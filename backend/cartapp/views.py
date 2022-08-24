from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from mainapp.models import Product
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import JsonResponse

# Create your views here.
from .models import Cart

main_menu = [
    {'href': 'main', 'active_if': ['main'], 'name': 'Домой'},
    {'href': 'products:index', 'active_if': ['product:index', 'product:category'], 'name': 'Продукты'},
    {'href': 'contacts', 'active_if': ['contacts'], 'name': 'Контакты'},
]


@login_required
def cart(request):
    products = request.user.cart.order_by('product__category')
    context = {
        'cart': products,
        'main_menu': main_menu

    }
    return render(request, 'cartapp/cart.html', context=context)


@login_required
def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)

    cart_product = request.user.cart.filter(id=pk).first()

    if not cart_product:
        cart_product = Cart(user=request.user, product=product)

    cart_product.quantity += 1
    cart_product.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def remove_from_cart(request, pk):
    cart_item = get_object_or_404(Cart, pk=pk)
    cart_item.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def api_edit_cart(request, pk, quantity):
    if request.is_ajax():
        quantity = int(quantity)
        new_cart_item = Cart.objects.get(pk=int(pk))
        if quantity > 0:
            new_cart_item.quantity = quantity
            new_cart_item.save()
        else:
            new_cart_item.delete()
        cart_items = cart.objects.filter(user=request.user).order_by('product__category')
        content = {
            'cart_items': cart_items,
        }
        result = render_to_string('cartapp/includes/inc_cart_list.html', content)

        return JsonResponse(
            {
                'result': result
            }
        )
