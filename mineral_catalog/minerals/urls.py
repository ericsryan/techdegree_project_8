"""mineral_catalog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.mineral_list, name='list'),
    path('by-letter/<letter>/',
         views.mineral_list_by_letter,
         name='mineral_list_by_letter'
    ),
    path('by-group/<group>/',
         views.mineral_list_by_group,
         name='mineral_list_by_group'
    ),
    path('by-color/<color>/',
         views.mineral_list_by_color,
         name='mineral_list_by_color'
    ),
    path('results/',
         views.search_minerals,
         name='search'
    ),
    path('random/', views.random_mineral_detail, name='random'),
    path('<slug:pk>/', views.mineral_detail, name='detail'),
]
