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
    path('add_products/', views.add_product, name='add_product'),
    path('del_product/<int:ID>/', views.delete_product, name='del_product'),
    path('product_details/<int:ID>/', views.products_details, name='product_details'),

    # rel-products
    path('add_rel_products/<int:product_id>/', views.add_rel_product, name='add_rel_product'),
    path('del_rel_products/<int:ID>/<int:current_page>/', views.delete_rel_product, name='del_rel_product'),
    path('search_rel_products/', views.SearchRelProduct.as_view(), name='search_rel_products'),
    
]
