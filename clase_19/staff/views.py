from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def inicio(request):
    return HttpResponse("Esta es la página de inicio", request)

def index(request):
    return render('staff/index.html', request)