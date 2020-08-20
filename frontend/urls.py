from django.urls import path, re_path
from frontend import views

urlpatterns = [
    re_path(r'^.*\.html', views.pages, name='fpages'), 
    path('', views.index, name='index'),
    path('sub_cat_page/<int:ID>/', views.sub_cat_page, name='sub_cat_page'),
    path('get_sub_catagory/<int:ID>/', views.get_sub_catagories, name='get_sub_cat'),
]
