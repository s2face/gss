from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Poll dir index")
# Create your views here.
