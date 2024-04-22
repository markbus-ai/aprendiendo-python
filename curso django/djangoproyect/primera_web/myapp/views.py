from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("hola mundo")

def about(request):
    return HttpResponse("<h1>alo mi verdadero amor</h1>")