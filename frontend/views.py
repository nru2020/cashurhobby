from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
import json

from app.models import (
    Catagory,
    SubCatagory,
    Products
)

""" 
############################# ++++++++++++++++++++ #############################
                        ++++++++   Frontend  ++++++++      
############################# ++++++++++++++++++++ #############################
"""
# default pages loader
def pages(request):
    context = {}
    try:        
        load_template = request.path[1:]
        # file_name = request.path.split('/')[-1].split('.')[0]
        # file with data binding
        template = loader.get_template(load_template)
    except:
        # 404!
        template = loader.get_template('fpages/404.html')
    return HttpResponse(template.render(context, request))


def index(request):
    context = {
        'catagory_list': Catagory.objects.values('id', 'cat_name')
    }
    return render(request, 'index.html', context)

# catagory dropdown 
def get_sub_catagories(request, ID):
    obj = SubCatagory.objects.filter(par_cat=Catagory.objects.get(id=ID)).values('id', 'cat_name')
    qs_json = json.dumps(list(obj))
    # print(qs_json)
    return HttpResponse(qs_json)


def sub_cat_page(request, ID):
    obj = Products.objects.filter(catagory=SubCatagory.objects.get(id=ID))
    products = {
        'products': obj
    }
    return render(request, 'fpages/product.html', products)
