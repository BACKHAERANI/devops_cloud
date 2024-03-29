from django.urls import path
from shop import views

app_name = 'shop'

urlpatterns = [path('', views.shop_list, name='shop_list'),
               path('<int:pk>', views.shop_detail, name='shop_detail'),
               path('<int:pk>/edit/', views.shop_edit, name='shop_edit'),
               path('<int:pk>/delete/', views.shop_delete, name ='shop_delete'),
               path('new/', views.shop_new, name='shop_new'),
               path('<int:pk>/review/new/', views.review_new, name='review_new'),
               path('<int:shop_pk>/review/<int:pk>/edit', views.review_edit, name='review_edit'),
               path('<int:shop_pk>/review/<int:pk>/delete',views.review_delete, name='review_delete'),
               path("tags/<str:tag_name>/", views.tag_detail, name="tag_detail"),

               ]


