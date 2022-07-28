from django.contrib import admin
from django.urls import path

from HamaApp import views


urlpatterns = [

    path('',views.home),
    path('photos', views.photos, name='photos'),
    path('index', views.index, name='index'),
    path('gestion', views.gestion,name="gestion"),
    path('delete-gestion/<nom>', views.delete_gestion, name='delete-gestion'),
    path('mandat', views.mandat, name='mandat'),
    path('pdf_mandat', views.pdf_mandat, name='pdf_mandat'),
    path('pdf', views.pdf, name='pdf'),

]