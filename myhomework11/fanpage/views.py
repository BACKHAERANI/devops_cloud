from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from fanpage.models import Post


def index(request):
    return render(request, 'fanpage/index.html')


def post_list(request: HttpRequest) -> HttpResponse:
    request.GET
    request.POST
    request.FILES
    qs = Post.objects.all()
    qs = qs.order_by("-pk")

    q = request.GET.get("q", "")
    if q:
        qs = qs.filter(title__icontains=q)

    return render(request, "fanpage/post_list.html", {
        "post_list":qs,
    })

def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    post = Post.objects.get(pk = pk)
    return render(request, "fanpage/post_detail.html",{"post": post})