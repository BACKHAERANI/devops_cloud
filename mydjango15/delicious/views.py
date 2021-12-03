from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.views.generic import CreateView
from delicious.form import ShopForm
from delicious.models import Shop


def shop_list(request: HttpRequest) -> HttpResponse:
    qs = Shop.objects.all()
    #querystring에 guery 이름의 인자를 확인
    query = request.GET.get("query","")
    if query:
        qs = qs.filter(name__icontains=query)

    template_name = "delicious/shop_list.html"
    context_data = {
        "shop_list":qs,
    }
    return render(request,template_name,context_data)  #지정인자로 받기


def shop_detail(request:HttpRequest, pk: int) -> HttpResponse:
    shop = Shop.objects.get(pk= pk)
    template_name = "delicious/shop_detail.html"
    context_data={
        "shop": shop,
    }
    return render(request, template_name, context_data)


def shop_new_1(request:HttpRequest)->HttpResponse:
    if request.method == "GET":                          #파이썬은 대문자 아니면 소문자로 통일하여 post나 get 입력
        return render(request,"delicious/shop_form_1.html",{})
    else:
        name = request.POST["name"]
        description = request.POST["description"]
        address = request.POST["address"]
        latitude = request.POST["latitude"]
        longitude = request.POST["longitude"]
        telephone = request.POST["telephone"]
        # 유효성검사 필요
        Shop.objects.create(
            name=name,
            description=description,
            address=address,
            latitude=latitude,
            longitude=longitude,
            telephone=telephone,
        )
        return redirect("/delicious/")


shop_new = CreateView.as_view(
    model=Shop,
    form_class=ShopForm,
    success_url="/delicious/",
)