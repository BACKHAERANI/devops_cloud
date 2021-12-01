from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from fan.models import Post


def index(request):
    return render(request, 'fan/index.html')


def post_list(request:HttpRequest) -> HttpResponse:
    request.GET
    request.POST
    request.FILES
    qs = Post.objects.all()
    qs = qs.order_by("-pk")

    q = request.GET.get("q", "")
    if q:
        qs = qs.filter(title__icontains=q)

    return render(request, "fan/post_list.html", {
        "post_list":qs,
    })


def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    post = Post.objects.get(pk = pk)
    return render(request, "fan/post_detail.html",{"post":post})
