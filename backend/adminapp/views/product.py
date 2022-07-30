from django.core.exceptions import PermissionDenied
from mainapp.models import Product, ProductCategory
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import user_passes_test


def check_is_superuser(user):
    if not user.is_superuser:
        raise PermissionDenied
    return True


@user_passes_test(check_is_superuser)
def products(request, pk):
    title = 'админка/продукт'
    category = get_object_or_404(ProductCategory, pk=pk)
    products_list = Product.objects.filter(category__pk=pk).order_by('name')
    content = {
        'title': title,
        'category': category,
        'objects': products_list,
    }
    return render(request, 'adminapp/products.html', content)


@user_passes_test(check_is_superuser)
def product_create(request, pk):
    pass


@user_passes_test(check_is_superuser)
def product_read(request, pk):
    pass


@user_passes_test(check_is_superuser)
def product_update(request, pk):
    pass


@user_passes_test(check_is_superuser)
def product_delete(request, pk):
    pass
