#Class Based View -뷰 함수를 만들어 주는 클래스
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.forms import PostForm
from blog.models import Post


post_list = ListView.as_view(model=Post,)

post_detail = DetailView.as_view(model=Post,)

post_new = CreateView.as_view(model=Post, form_class=PostForm, success_url=reverse_lazy("blog:post_list"))

post_edit = UpdateView.as_view(model=Post, form_class=PostForm, success_url=reverse_lazy("blog:post_list"))

# reverse()가 안되는 이유 - 프로젝트 로딩 이후에 url reverse가 가능한데, reverse는 로딩 전에 시작됨 reverse_lazy는 필요할때만 호출
#  success_url="blog:post_list")  success는 url reverse를 적용하지 않는다.
# success_url="/blog/",)  #url 가변적으로 지정할 수 없다./ url reverse가 미적용됐다

post_delete = DeleteView.as_view(model=Post, success_url=reverse_lazy("blog:post_list"))

