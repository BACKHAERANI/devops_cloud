from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from wannaone.models import Star


def tag_detail(request: HttpRequest, tag_name:str) -> HttpResponse:
    qs = Star.objects.all()
    qs = qs.filter(tag_set__name=tag_name)
    return render(request, "wannaone/tag_detail.html", {"tag_detail":qs,})


def star_list(request: HttpRequest) -> HttpResponse:
    qs = Star.objects.all()
    query = request.GET.get("query", "")
    if query:
        qs = qs.filter(name__icontains=query)
    return render(request, "wannaone/star_list.html", {"star_list": qs, })


def star_detail(request: HttpRequest, pk: int) -> HttpResponse:
    star = Star.objects.get(pk=pk)
    return render(request, "wannaone/star_detail.html", {"star": star})