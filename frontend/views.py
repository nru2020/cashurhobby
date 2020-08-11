from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader

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
        print(load_template)
        # file_name = request.path.split('/')[-1].split('.')[0]
        # file with data binding
        template = loader.get_template(load_template)
    except:
        # 404!
        template = loader.get_template('fpages/404.html')
    return HttpResponse(template.render(context, request))


def index(request):
    return render(request, 'index.html')
    