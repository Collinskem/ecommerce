
from django.shortcuts import render, get_object_or_404,redirect
from .models import Category, Product
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'shop/Products/list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }
    return render(request, 'shop/products/detail.html', context)

def index (request):
    products = Product.objects.filter(available=True)
    context = {

        'products': products
    }
    return render (request, 'shop/index.html',context)

def about (request):
    return render(request,'shop/about.html')
def contact (request):
    return render(request,'shop/contact.html')
