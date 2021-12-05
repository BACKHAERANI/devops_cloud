from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from hwangridangil.models import Shop


def shop_list(request: HttpRequest) -> HttpResponse:
    qs = Shop.objects.all()
    template_name = "hwangridangil/shop_list.html"
    context_data = {"shop_list": qs}
    return render(request,template_name,context_data)


def shop_detail(request: HttpRequest) -> HttpResponse:
    shop = Shop.objects.all()
    template_name = "hwangridangil/shop_detail.html"
    context_data = {"shop":shop}
    return render(request,template_name,context_data)
