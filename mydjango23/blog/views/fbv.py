from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from blog.forms import PostForm
from blog.models import Post


def post_list(request:HttpRequest) -> HttpResponse:
    post_qs = Post.objects.all()
    format = request.GET.get("format","")  # format이라는 이름의 querystring을 가져옴./
    if format == "xlsx":
        tabular_data = Post.get_tabular_data(post_qs, format="xlsx")

        return HttpResponse(tabular_data, content_type="application/vnd.ms-excel")

    return render(request, "blog/post_list.html", {"post_list": post_qs})


def post_detail(request:HttpRequest, pk:int) -> HttpResponse:
    post = get_object_or_404(Post, pk=pk)
    return render(request, "blog/post_detail.html", {"post": post})


def post_new(request:HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            saved_post = form.save()
            messages.success(request, "새로운 포스팅을 저장했습니다.")
            return redirect(saved_post)
    else:
        form = PostForm()

    return render(request, "blog/post_form.html", {"form":form})


def post_edit(request: HttpRequest, pk:int) -> HttpResponse:
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            saved_post = form.save()
            messages.success(request, f"#{pk}번째 포스팅을 저장했습니다.")
            return redirect( saved_post)
    else:
        form = PostForm(instance=post)

    return render(request, "blog/post_form.html", {"form":form, "post": post,})


def post_delete(request:HttpRequest, pk:int) -> HttpResponse:
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        messages.success(request, f"#{pk}번째 포스팅을 삭제했습니다.")
        return redirect("blog:post_list")
    return render(request, "blog/post_confirm_delete.html", {"post": post})


