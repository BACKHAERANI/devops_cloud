from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.views.generic import CreateView

from hwangridan.models import Shop


def shop_list(request: HttpRequest) -> HttpResponse:
    qs = Shop.objects.all()
    query = request.GET.get("query","")
    if query:
        qs= qs.filter(name__icontains=query)
    template_name = "hwangridan/shop_list.html"
    context_data ={"shop_list":qs, }
    return render(request,template_name, context_data)


def shop_detail(request: HttpRequest, pk: int) -> HttpResponse:
    shop = Shop.objects.get(pk=pk)
    template_name = "hwangridan/shop_detail.html"
    context_data = {"shop": shop,}
    return render(request, template_name,context_data)


def shop_new_1(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return render(request, "hwangridan/shop_form.html", {})
    else:
        name = request.POST["name"]
        description = request.POST["description"]
        photo = request.POST["photo"]
        address = request.POST["address"]
        latitude = request.POST["latitude"]
        longitude = request.POST["longitude"]
        telephone = request.POST["telephone"]
        Shop.objects.create(
            name=name,
            description=description,
            photo=photo,
            address=address,
            latitude=latitude,
            longitude=longitude,
            telephone=telephone,
        )
        return redirect('/hwangridan/')


shop_new = CreateView.as_view(
    model=Shop,
    form_class=ShopForm,
    success_url="/hwangridan/"
)