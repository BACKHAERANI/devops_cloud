from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from shop import views


app_name = 'shop'


urlpatterns=[path('new/', views.shop_new, name="shop_new"),
             path('<int:pk>/', views.shop_detail, name="shop_detail"),]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns +=['__debug__/', include(debug_toolbar.urls),]