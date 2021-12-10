from django.urls import path
from shop import views


app_name = 'shop'


urlpatterns=[path('new/', views.shop_new, name="shop_new"),
             path('<int:pk>/', views.shop_detail, name="shop_detail"),]
