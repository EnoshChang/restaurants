"""restaurants URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# from .views import del_restaurant, menu, index, taiwan_rest, new_restaurant, edit_restaurant, del_restaurant, foods
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/', views.menu),
    path('index/', views.index),
    path('restaurants/', views.taiwan_rest),
    path('restaurant/new/', views.new_restaurant),
    path('restaurant/<int:r_id>/edit/', views.edit_restaurant),
    path('restaurant/<int:r_id>/del/', views.del_restaurant),
    path('restaurant/<int:r_id>/foods/', views.foods),
    path('restaurant/<int:r_id>/food/new/', views.new_food),
    path('restaurant/<int:r_id>/food/<int:f_id>/edit/', views.edit_food),
    path('restaurant/<int:r_id>/food/<int:f_id>/del/', views.del_food)
]
