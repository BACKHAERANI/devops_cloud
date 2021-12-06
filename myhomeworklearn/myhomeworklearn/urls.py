from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from learn.views import show_list, show_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('learn/', show_list),
    path('learn/<int:pk>/', show_detail),
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__', include(debug_toolbar.urls)),
                    ]