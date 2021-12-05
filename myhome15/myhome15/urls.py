from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from hwangridan.views import shop_list, shop_detail, shop_new_1, shop_new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hwangridan/', shop_list),
    path('hwangridan/<int:pk>/', shop_detail),
    path('hwangridan/new1/', shop_new_1),
    path('hwangridan/new/', shop_new),
]


urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns +=[path('__debug__', include(debug_toolbar.urls)),]

