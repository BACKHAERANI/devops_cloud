from django.urls import path
from blog.views import fbv as views
# from blog.views import cbv as views    #as views :views라고 부르겠다

app_name = 'blog'

urlpatterns = [path('', views.post_list, name='post_list'),
               path('<int:pk>/', views.post_detail, name='post_detail'),
               path('<int:pk>/edit', views.post_edit, name ='post_edit'),
               path('new/', views.post_new, name='post_new'),
               path('<int:pk>/delete/', views.post_delete, name='post_delete'),
               path('subscriber/', views.subscriber_new, name= 'subscriber_new'),]