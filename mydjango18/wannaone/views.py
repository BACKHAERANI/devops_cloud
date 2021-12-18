from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from wannaone.form import StarForm
from wannaone.models import Star


def tag_detail(request: HttpRequest, tag_name: str) -> HttpResponse:
    qs = Star.objects.all()
    qs = qs.filter(tag_set__name=tag_name)
    return render(request, "wannaone/tag_detail.html", {"tag_name":tag_name, "star_list":qs})


def star_list(request: HttpRequest) -> HttpResponse:
    qs = Star.objects.all()
    query = request.GET.get("query", "")
    if query:
        qs = qs.filter(name__icontains=query)
    return render(request, "wannaone/star_list.html", {"star_list": qs, })


def star_detail(request: HttpRequest, pk: int) -> HttpResponse:
    star = Star.objects.get(pk=pk)
    tag_list = star.tag_set.all()
    return render(request, "wannaone/star_detail.html", {"star": star,  "tag_list" : tag_list})

def star_new(request: HttpRequest) ->HttpResponse:
    if request.method = "POST":
        form = StarForm(request.POST, request.FILES)
        if form.is_vaild():
            star = form.save(commit=False)
            star.ip = request.META("REMOTE_ADDR")
            form.save()
            messages.success(request, "성공적으로 등록되었습니다.")
            return redirect("wannaone:star_list")
        else:
            form = StarForm

        return render(request, "wannaone/star_form.html",{"form":form})

