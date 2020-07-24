from django.urls import path, re_path
from app import views

urlpatterns = [
    re_path(r'^.*\.html', views.pages, name='pages'), # PagesManager
    path('', views.home, name='Home_page'),

    # catagory   
    path('add_catagory/',views.add_catagory, name='add_cat'),
    path('del_catagory/<int:ID>/', views.delete_catagory, name='del_cat'),
    path('detail_catagory/<int:ID>/', views.detail_catagory, name='cat_detail'),

    # subcatagory    
    path('add_subcatagory/', views.add_subcatagory, name="add_subcat"),
    path('del_subcatagory/<int:ID>/', views.delete_subcatagory, name="del_subcat"),
    path('detail_subcatagory/<int:ID>/', views.details_subcatagory, name="subcat_details"),

    # products
    
]
