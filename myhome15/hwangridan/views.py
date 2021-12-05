from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from hwangridan.models import Shop


def shop_list(request: HttpRequest) -> HttpResponse:
    qs = Shop.objects.all()
    template_name = "hwangridan/shop_list.html"
    context_data ={"shop_list":qs, }
    return render(request,template_name, context_data)


def shop_detail(request: HttpRequest, pk:int) -> HttpResponse:
    shop = Shop.objects.get(pk=pk)
    template_name = "hwangridan/shop_detail"
    context_data = {"shop": shop,}
    return render(request, template_name,context_data)