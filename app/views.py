from django.core import serializers
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.template import loader

from .models import (
    Catagory,
    SubCatagory, 
    Products,
    RelProducts,
    ProductsReview,
)
from .forms import (
    CatagoryForm, 
    SubCatagoryForm, 
    ProductBasicInfoForm,
    ProductPriceInventoryForm,
    ProductShippingForm,
    RelProductsForm,
)


def pages(request):
    context = {}
    try:        
        load_template = request.path[1:]
        file_name = request.path.split('/')[-1].split('.')[0]

        # file with data binding
        if (file_name == 'catagory'):
            context['catagory'] = Catagory.objects.all().order_by('-id')

        if (file_name == 'products'):
            context['products'] = Products.objects.all().order_by('-id')
            
        template = loader.get_template(load_template)
    except:
        # 404!
        template = loader.get_template('pages/404.html')
    return HttpResponse(template.render(context, request))


def home(request):
    return render(request, 'pages/index.html')


""" Catagory """
# CRUD Catagory
def add_catagory(request):
    if request.method == 'POST':
        try:
            catagory_name= request.POST['catagory']
            obj = Catagory.objects.create(
                cat_name=catagory_name
            )
            if obj is None:
                return JsonResponse({'success':False})
            return JsonResponse({'success':True})
        except:
            pass
    return JsonResponse({'success':False})


def delete_catagory(request, ID):
    if Catagory.objects.filter(id=ID).exists():
        obj = Catagory.objects.get(id=ID)
        obj.delete()
        return HttpResponseRedirect('/pages/catalog/catagory.html')    
    return HttpResponseRedirect('/pages/catalog/catagory.html')    


def detail_catagory(request, ID):
    if request.method == 'POST':
        form = CatagoryForm(data=request.POST, files=request.FILES, instance=Catagory.objects.get(id=ID))
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False})

    if Catagory.objects.filter(id=ID).exists():
        obj = Catagory.objects.get(id=ID)
    
        context = {
            'sub_catagory': SubCatagory.objects.filter(par_cat=Catagory.objects.get(pk=ID)).order_by('-id'),
            'update_catagory_form': CatagoryForm(instance=obj)
        }
        return render(request, 'pages/catalog/cat_details.html', context)
    return HttpResponseRedirect('/pages/catalog/catagory.html')    


""" Sub Catagory """
# subcatagory
def add_subcatagory(request):
    if request.method == 'POST':
        try:
            catagory_name = request.POST['catagory']
            parent_catagory = request.POST['par_cat']
            obj = SubCatagory.objects.create(
                cat_name=catagory_name,
                par_cat=Catagory.objects.get(pk=parent_catagory)
            )
            
            if obj is None:
                return JsonResponse({'success':False, 'msg': 'Something went wrong! Not saved!'})
            return JsonResponse({'success':True, 'msg': 'Successfully Added!'})
        except:
            pass
    return JsonResponse({'success':False})


def delete_subcatagory(request, ID):
    if SubCatagory.objects.filter(id=ID).exists():
        obj = SubCatagory.objects.get(id=ID)
        obj.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})


def details_subcatagory(request, ID):
    if request.method == 'POST':
        form = SubCatagoryForm(data=request.POST, files=request.FILES, instance=SubCatagory.objects.get(id=ID))
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False})

    if SubCatagory.objects.filter(id=ID).exists():
        obj = SubCatagory.objects.get(id=ID)    
        context = {
            'update_subcatagory_form': SubCatagoryForm(instance=obj)
        }
        return render(request, 'pages/catalog/sub_cat_details.html', context)
    return HttpResponseRedirect('/pages/catalog/catagory.html')    


""" Products """
def add_product(request):
    if request.method == 'POST':
        try:
            product_name = request.POST['prod_name']
            obj = Products.objects.create(
                prod_name=product_name
            )
            if obj is None:
                return JsonResponse({'success':False})
            return JsonResponse({'success':True})
        except:
            print('error')
    return JsonResponse({'success':False})

# rel-product
def add_rel_product(request, product_id):
    if request.method == 'POST':
        try:
            product_names = request.POST['prod_id_list'].split(',')
            for i in product_names:                
                obj = RelProducts.objects.create(
                    prod_id=Products.objects.get(id=product_id),
                    rel_prod=Products.objects.get(id=i)
                )
            return JsonResponse({'success':True})
        except:
            pass
    return JsonResponse({'success':False})

# del related products
def delete_rel_product(request, ID, current_page):
    if RelProducts.objects.filter(id=ID).exists():
        obj = RelProducts.objects.get(id=ID)
        obj.delete()
        return HttpResponseRedirect(f'/product_details/{current_page}/')    
    return HttpResponseRedirect(f'/product_details/{current_page}/')    


# (!error going on) related product search
def search_rel_product(request):
    if request.method == 'POST':
        search_text = request.POST['search_text']
        serializer = serializers.serialize("json", Products.objects.filter(prod_name__icontains=search_text))
        data = {"searched_data": serializer}
        return JsonResponse(data)
    return JsonResponse({'success': False})


# del products
def delete_product(request, ID):
    if Products.objects.filter(id=ID).exists():
        obj = Products.objects.get(id=ID)
        obj.delete()
        return HttpResponseRedirect('/pages/catalog/products.html')    
    return HttpResponseRedirect('/pages/catalog/products.html')    

def products_details(request, ID):
    # if post
    if request.method == 'POST':
        form1 = ProductBasicInfoForm(data=request.POST or None, files=request.FILES, instance=Products.objects.get(id=ID))
        form2 = ProductPriceInventoryForm(data=request.POST or None, instance=Products.objects.get(id=ID))
        form3 = ProductShippingForm(data=request.POST or None, instance=Products.objects.get(id=ID))
        
        if form1.is_valid():
            # print('form1')
            form1.save()
            return JsonResponse({'success': True})
        elif form2.is_valid():
            # print('form2')
            form2.save()
            return JsonResponse({'success': True})
        elif form3.is_valid():
            # print('form3')
            form3.save()
            return JsonResponse({'success': True})
        else:
            # not validated
            # print(form3.errors.as_data())
            return JsonResponse({'success': False})
    
    if Products.objects.filter(id=ID).exists():
        obj = Products.objects.get(id=ID)    
        context = {
            'all_products':Products.objects.all(),
            'current_id':ID,
            'related_products':RelProducts.objects.filter(prod_id=ID),
            'product_reviews': ProductsReview.objects.filter(prod_id=ID),

            'related_product_form': RelProductsForm(instance=obj),
            'product_basic_form': ProductBasicInfoForm(instance=obj),
            'product_price_inventory_form': ProductPriceInventoryForm(instance=obj),
            'product_shipping_form': ProductShippingForm(instance=obj),
            'catagory_form': SubCatagoryForm(),
        }
        return render(request, 'pages/catalog/product_detail.html', context)
    return HttpResponseRedirect('/pages/catalog/products.html')    
