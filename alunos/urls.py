from django.urls import path

from . import views

urlpatterns = [
    path("create/", views.adicionar, name="adicionar"),
    path("remove/", views.remover, name="romover"),
    path("lista/", views.listar, name="listar"),
    path("atualizar/", views.atualiza, name="atualizar"),     
       
]
