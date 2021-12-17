from django.urls import path

from shop import views

app_name='shop'

urlpatterns = [path('', views.shop_list, name='shop_list'),
               path('<int:pk>/', views.shop_detail, name='shop_detail'),
               path('<int:shop_pk>/reviews/new/', views.review_new, name = "review_new"),
               path('<int:shop_pk>/reviews/<int:pk>/edit/', views.review_edit, name="review_edit"),


               ]     #urlpatterns는 빈 리스트라도 무조건 있어야 한다.