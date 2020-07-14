from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .forms import CatagoryForm

def pages(request):
    x = CatagoryForm()
    context = {'editor_summernote':x}
    try:        
        load_template = request.path[1:]
        # print(request.path, load_template)
        template = loader.get_template(load_template)
    except:
        # 404!
        template = loader.get_template('pages/404.html')
    return HttpResponse(template.render(context, request))

def home(request):
    return render(request, 'pages/index.html')