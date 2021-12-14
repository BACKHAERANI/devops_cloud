from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest,HttpResponse
from shop.forms import ShopForm, ReviewForm
from shop.models import Shop, Category, Review


def shop_list(request:HttpRequest) -> HttpResponse:
    category_qs = Category.objects.all()
    shop = Shop.objects.all()

    category_id:str = request.GET.get("category_id","")
    if category_id:
        shop = shop.filter(category__pk=category_id)

    query = request.GET.get("query","")
    if query:
        shop = shop.filter(name__icontains=query)

    return render(request, "shop/shop_list.html",{"shop_list":shop, "category_list": category_qs})


def shop_detail(request:HttpRequest, pk:int) -> HttpResponse:
    shop = get_object_or_404(Shop, pk=pk)
    tag_list = shop.tag_set.all()
    review_list = shop.review_set.all()
    return render(request, "shop/shop_detail.html", {"shop":shop, "tag_list":tag_list, "review_list": review_list})


def shop_new(request:HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ShopForm(request.POST, request.FILES)
        if form.is_valid():
            saved_shop = form.save()
            messages.success(request, "성공적으로 저장했습니다.")
            return redirect("shop:shop_detail", saved_shop.pk)
    else:
        form = ShopForm
    return render(request, "shop/shop_form.html", {"form": form})


def shop_edit(request:HttpRequest, pk:int) -> HttpResponse:
    shop = get_object_or_404(Shop, pk=pk)
    if request.method == "POST":
        form = ShopForm(request.POST, request.FILES, instance=shop)
        if form.is_valid():
            form.save()
            return redirect("shop:shop_detail", pk)
    else:
        form = ShopForm(instance=shop)

    return render(request, "shop/shop_form.html", {"form": form})


def tag_detail(request:HttpRequest, tag_name:str) -> HttpResponse:
    qs = Shop.objects.all()
    qs = qs.filter(tag_set__name=tag_name)
    return render(request,
                  "shop/tag_detail.html",
                  {"tag_name":tag_name, "shop_list": qs})


def review_new(request: HttpRequest, shop_pk: int) -> HttpResponse:
    shop = get_object_or_404(Shop, pk=shop_pk)

    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.shop = shop
            review.save()
            return redirect("shop:shop_detail", shop_pk)
    else:
        form = ReviewForm()
    return render(request, "shop/review_form.html", {"form": form})


def review_edit(request:HttpRequest, pk:int, shop_pk:int) -> HttpResponse:
    review = get_object_or_404(Review, pk=pk)
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            return redirect("shop:shop_detail", shop_pk )
    else:
        form = ReviewForm(instance=review)

    return render(request, "shop/shop_form.html", {"form": form})