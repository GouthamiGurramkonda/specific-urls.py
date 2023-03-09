from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def virat(request):
    return HttpResponse('<h1>virat best batman in the world</h1>')


def surya(request):
    return HttpResponse('<h1>surya is best cricketer</h1>')
