from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hola a todos!!!")

#1.Creo la vista es decir na funcion