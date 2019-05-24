from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest

def index(request):
    return HttpResponse("root dir <br> Application: <a href=http://127.0.0.1:8000/polls/>Poll</a>")

def ls(reqest):
   # a=HttpRequest.path_info
    return HttpResponse('asd +a')# % str(a))




# Create your views here.
