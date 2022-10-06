from django.shortcuts import render
from .models import *
import requests

def index(request):
    products=Product.objects.all()
    context={'products':products}
    return render(request, 'index.html', context)

def product(request, product_id):
    product=Product.objects.get(pk=product_id)
    last_viewed_product=None

    if 'last_viewed' in request.session:
        if product_id in request.session['last_viewed']:
            request.session['last_viewed'].remove(product_id)

        products=Product.objects.filter(pk__in=request.session['last_viewed'])
        last_viewed_product=sorted(products, key=lambda x: request.session['last_viewed'].index(x.id))
        request.session['last_viewed'].insert(0, product_id)
        if(len(request.session['last_viewed'])>5):
            request.session['last_viewed'].pop()
    else:
        request.session['last_viewed']=[product_id]

    request.session.modified=True      #Tells Django to update session even when no changes are made
    
    context={'product':product, 'last_viewed_product':last_viewed_product}
    return render(request, 'product.html', context)

def view_product(request):
    r=requests.get('https://fakestoreapi.com/products')
    print(r.json())
    for item in r.json():
        product=Product(
            title=item['title'],
            description=item['description'],
            price=item['price'],
            image_url=item['image']
        )
        product.save()
    return render(request, 'index.html')