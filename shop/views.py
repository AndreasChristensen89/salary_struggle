from django.shortcuts import render, get_object_or_404
from django.db.models.functions import Lower
from .models import Product
from .forms import ProductForm


def all_products(request):
    """ A view to return the products page """
    
    products = Product.objects.all()
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                product = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'current_sorting': current_sorting,
    }

    return render(request, 'shop/products.html', context)


def product_details(request, item_id):
    """ A view to return the item details page """

    product = get_object_or_404(Product, pk=item_id)

    context = {
        'product': product,
    }

    return render(request, 'shop/product_details.html', context)


def add_product(request):
    """ Add a product to the store """
    form = ProductForm()
    template = 'shop/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
