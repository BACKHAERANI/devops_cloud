from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

def index(request:HttpRequest) -> HttpResponse:
    return render(request,"dogtube/index.html")