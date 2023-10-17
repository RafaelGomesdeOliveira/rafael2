from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def adicionar(request):
    return HttpResponse("Aqui adiciona")

def listar(request):
    return HttpResponse("Aqui lista")

def remover(request):
    return HttpResponse("Aqui remove")

def atualiza(request):
    return HttpResponse("Aqui atualiza")