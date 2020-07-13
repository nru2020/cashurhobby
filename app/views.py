from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def pages(request):
    context = {}
    try:        
        load_template = request.path[1:]
        # print(request.path, load_template)
        template = loader.get_template(load_template)
    except:
        # 404!
        template = loader.get_template('pages/examples/404.html')
    return HttpResponse(template.render(context, request))

def home(request):
    return render(request, 'pages/index.html')