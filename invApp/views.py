from django.shortcuts import render

# Create your views here.
from .forms import ProductForm
from .models import Product 

# CURD = create , update and delete
# Home View
def home_view(request):
    return render(request, 'invApp/home.html')


#create view
def product_create_view(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')

    return render(request, 'invApp/product_form.html', {'form':form})

# read view

def product_list_view(request):
    product = Product.objects.all()
    return render(request, 'invApp/product_list.html', {'products': product} )

# update view

def product_update_view(request, product_id):
    Product.objects.get(product_id=product_id) # get is a specail method which gonna target product_id
    form = ProductForm(instance = product)
    if request.method == "POST":
        form = ProductForm(request.POST, instance= product)
        if form.is_valid:
            form.save
            return redirect('product_list')
    return render(request, 'invApp/product_form.html', {'form':form})

# delete view
def product_delete_view(request, product_id):
    Product.objects.get(product_id=product_id) # get is a specail method which gonna target product_id
    form = ProductForm(instance = product)
    if request.method == "POST":
        product.delete()
        return redirect('product_list')
    return render(request, 'invApp/product_confirm_delete.html',{'product':product})






