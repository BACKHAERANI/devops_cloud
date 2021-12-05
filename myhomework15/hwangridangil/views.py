from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from hwangridangil.models import Shop


def shop_list(request: HttpRequest) -> HttpResponse:
    qs = Shop.objects.all()
    query = request.GET.get("guery", "")
    if query:
        qs = qs.filter(name__icontains=query)
    template_name = "hwangridangil/shop_list.html"
    context_data = {"shop_list": qs,}
    return render(request,template_name,context_data)


def shop_detail(request: HttpRequest, pk:int) -> HttpResponse:
    shop = Shop.objects.get(pk=pk)
    template_name = "hwangridangil/shop_detail.html"
    context_data = {"shop": shop,}
    return render(request,template_name,context_data)
