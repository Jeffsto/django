from django.shortcuts import render
from .models import Product
from .forms import ProductForm
from django.conf import settings
# Create your views here.

def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description
    # }
    context = {
        'object': obj,
    }
    return render(request, "products/product_detail.html", context)

def product_create_view(request):
    context = {}
    if request.method == "POST":
        my_new_title = request.POST.get(title=my_new_title)
        print(my_new_title)
        # Product.ojbects.create(title=my_new_title)
    return render(request, "products/product_create.html", context)

# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm()
#     context = {
#         'form': form,
#     }
#     return render(request, "products/product_create.html", context)
