from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows/new', views.newShow),
    path('addShow', views.addShow),
    path('shows', views.shows),
    path('shows/<int:id_show>', views.detalleshow),
    path('shows/<int:id_show>/edit', views.detalleditshow),
    path('editShow/<int:id_show>', views.editShow),
    path('shows/<int:id_show>/destroy', views.destroy),
    #path('process_money', views.process_money),
    #path('random_word/reset',views.cerrar_sesion),
    ]