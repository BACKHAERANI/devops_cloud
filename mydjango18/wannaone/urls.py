from wannaone import views
from django.urls import path

app_name = "wannaone"

urlpatterns = [path("", views.star_list, name="star_list"),
               path("<int:pk>", views.star_detail, name="star_detail"),
               ]
