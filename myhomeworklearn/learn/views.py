from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from learn.models import Show


def show_list(request: HttpRequest) -> HttpResponse:
    qs = Show.objects.all()
    template_name = "learn/show_list.html"
    context_data ={"show_list": qs,}
    return render(request, template_name, context_data)


def show_detail(request: HttpRequest, pk: int) -> HttpResponse:
    show = Show.objects.get(pk=pk)
    template_name = "learn/show_detail.html"
    context_data = {"show": show,}
    return render(request, template_name, context_data)




