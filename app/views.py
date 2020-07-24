from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.template import loader
from .models import Catagory, SubCatagory, Products
from .forms import CatagoryForm, SubCatagoryForm


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
