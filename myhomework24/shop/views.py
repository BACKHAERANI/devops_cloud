from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from shop.forms import ShopForm, ReviewForm
from shop.models import Shop, Review, Tag

shop_list = ListView.as_view(model=Shop, template_name="shop/shop_list.html")

shop_detail = DetailView.as_view(model=Shop, template_name="shop/shop_detail.html")

shop_new = CreateView.as_view(model=Shop, form_class=ShopForm)

shop_edit = UpdateView.as_view(model=Shop, form_class=ShopForm)

shop_delete = DeleteView.as_view(model=Shop, success_url=reverse_lazy("shop:shop_list"))

review_new = CreateView.as_view(model=Review, form_class=ReviewForm)

review_edit = UpdateView.as_view(model=Review, form_class=ReviewForm)

review_delete = DeleteView.as_view(model=Review, success_url=reverse_lazy("shop:shop_list"))

tag_detail = ListView.as_view(model=Tag,template_name="shop/tag_detail.html")