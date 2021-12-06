from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from hrdan.models import Shop


def shop_list(request: HttpRequest) -> HttpResponse:
    qs = Shop.objects.all()
    template_name = "hrdan/shop_list.html"
    context_data = {"shop_list": qs,}
    return render(request, template_name, context_data)

