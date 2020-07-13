from django.urls import path, re_path
from app import views

urlpatterns = [
    re_path(r'^.*\.html', views.pages, name='pages'), # PagesManager
    path('', views.home, name='Home_page'),
]
