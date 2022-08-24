from django.core.exceptions import PermissionDenied
from django.shortcuts import HttpResponseRedirect, get_object_or_404
from django.urls import reverse
from mainapp.models import Product, ProductCategory
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from authapp.forms import ShopUserRegisterForm
from adminapp.forms import ProductCategoryEditForm


def check_is_superuser(user):
    if not user.is_superuser:
        raise PermissionDenied
    return True


@user_passes_test(check_is_superuser)
def categories(request):
    title = 'админка/категории'
    categories_list = ProductCategory.objects.all()
    content = {
        'title': title,
        'objects': categories_list
    }
    return render(request, 'adminapp/categories.html', content)


@user_passes_test(check_is_superuser)
def category_create(request):
    title = 'Категории/создание'
    category_form = ProductCategoryEditForm()
    if request.method == 'POST':
        category_form = ProductCategoryEditForm(data=request.POST)
        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect(reverse('admin:categories'))

    content = {'title': title, 'update_form': category_form }
    return render(request, 'adminapp/category_create.html', content)


@user_passes_test(check_is_superuser)
def category_update(request, pk):
    title = 'Категории/редактирование'
    category = get_object_or_404(ProductCategory, pk=pk)
    update_form = ProductCategoryEditForm(instance=category)
    if request.method == "POST":
        update_form = ProductCategoryEditForm(instance=category, data=request.POST)
        if update_form.is_valid():
            update_form.save()
            return HttpResponseRedirect(reverse("admin:categories"))

    content = {
        "title": title,
        "category": category,
        "update_form": update_form,
            }
    return render(request, "adminapp/category_update.html", content)


@user_passes_test(check_is_superuser)
def category_delete(request, pk):
    title = 'Удаление категории'
    category = get_object_or_404(ProductCategory, pk=pk)

    if request.method == 'POST':
        category.is_active = False
        category.save()
        return HttpResponseRedirect(reverse("admin:categories"))

    content = {
        'tittle': title,
        'category_to_delete': category
    }
    return render(request, 'adminapp/category_delete.html', content)
