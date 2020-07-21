from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.template import loader
from .models import Catagory, SubCatagory
from .forms import CatagoryForm

def pages(request):
    x = CatagoryForm()
    context = {'editor_summernote':x}
    try:        
        load_template = request.path[1:]
        file_name = request.path.split('/')[-1].split('.')[0]

        # file with data binding
        if (file_name == 'catagory'):
            context['catagory'] = Catagory.objects.all().order_by('-id')


        template = loader.get_template(load_template)
    except:
        # 404!
        template = loader.get_template('pages/404.html')
    return HttpResponse(template.render(context, request))


def home(request):
    return render(request, 'pages/index.html')

# CRUD Catagory
def add_catagory(request):
    if request.method == 'POST':
        try:
            catagory_name= request.POST['catagory']
            obj = Catagory.objects.create(
                cat_name=catagory_name
            )
            if obj is None:
                return JsonResponse({'success':False, 'msg': 'Something went wrong! Not saved!'})
            return JsonResponse({'success':True, 'msg': 'Successfully Added!'})
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
    if Catagory.objects.filter(id=ID).exists():
        obj = Catagory.objects.get(id=ID)
    
        context = {
            'sub_catagory': SubCatagory.objects.filter(pk=ID).order_by('-id'),
            'update_catagory_form': CatagoryForm(instance=obj)
        }
        return render(request, 'pages/catalog/cat_details.html', context)
    return HttpResponseRedirect('/pages/catalog/catagory.html')    
    