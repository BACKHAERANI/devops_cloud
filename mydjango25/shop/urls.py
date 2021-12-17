from django.urls import path

from shop import views

app_name='shop'

urlpatterns = [path('', views.shop_list, name='shop_list'),
               path('<int:pk>/', views.shop_detail, name='shop_detail'),


               ]     #urlpatterns는 빈 리스트라도 무조건 있어야 한다.