from django.urls import path
from blog.views import fbv

app_name = 'blog'

urlpatterns = [path('', fbv.post_list, name='post_list'),
               path('<int:pk>/', fbv.post_detail, name='post_detail'),
               path('<int:pk>/edit', fbv.post_edit, name ='post_edit'),
               path('new/', fbv.post_new, name='post_new'),
               path('<int:pk>/delete/', fbv.post_delete, name='post_delete')]