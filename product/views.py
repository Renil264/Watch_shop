from django.views.generic import ListView, TemplateView

from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.urls import reverse

from product.models import ProductCategory, Product, Basket, FilterBrand, FilterCountry, FilterMaterial


def index(request):
    context = {
        'title': 'Главная',
        'products': Product.objects.all()[:3],
    }

    return render(request, 'product/index.html', context)


def product(request, category_id=None, page=1, brand=None, country=None, material=None, sort=None):
    q = request.GET.get('q')
    context = {
        'title': 'Каталог',
        'categories': ProductCategory.objects.all(),
        'filter_by_brand': FilterBrand.objects.order_by('brand'),
        'filter_by_country': FilterCountry.objects.order_by('country'),
        'filter_by_material': FilterMaterial.objects.order_by('material'),
    }
    if q:
        products = Product.objects.filter(name__icontains=q)
    elif category_id:
        products = Product.objects.filter(category_id=category_id)
    elif country:
        products = Product.objects.filter(country=country)
    elif brand:
        products = Product.objects.filter(brand_name=brand)
    elif material:
        products = Product.objects.filter(case_material=material)
    elif sort:
        if sort == "cheaper":
            products = Product.objects.order_by('price')
        elif sort == "expensive":
            products = Product.objects.order_by('-price')
    else:
        products = Product.objects.all()
    paginator = Paginator(products, 9)
    product_paginator = paginator.page(page)
    context.update({'products': product_paginator})

    return render(request, 'product/products.html', context)


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_delete(request, id):
    basket = Basket.objects.get(id=id)
    basket.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def checkout(request):
    basket = Basket.objects.all()
    basket.delete()

    return render(request, 'product/thanks.html')


def search(request):
    search_query = request.GET.get('search')
    context = {
        'products': Product.objects.filter(name__icontains=search_query),
        'search': search_query
    }

    return render(request, 'product/products.html', context)


def product_details(request, prod_id=None):
    context = {
        'title': 'Товар',
        'product_detail': Product.objects.get(id=prod_id),
    }

    context['products'] = Product.objects.filter(case_material=context['product_detail'].case_material)
    context['length'] = len(context['products'])

    return render(request, 'product/product_details.html', context)


def privacy(request):
    return render(request, 'product/privacy_policy.html')
