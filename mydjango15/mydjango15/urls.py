from django.contrib import admin
from django.urls import path
from delicious.views import shop_list, shop_detail


urlpatterns = [
    path('admin/', admin.site.urls),
    path('delicious/', shop_list),
    path('delicious/<int:pk>/', shop_detail),
]
