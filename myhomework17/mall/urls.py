from django.urls import path
from mall import views


app_name = "mall"

urlpatterns = [path("", views.shop_list, name="shop_list"),
               path("<int:pk>/", views.shop_detail, name="shop_detail"),
               ]