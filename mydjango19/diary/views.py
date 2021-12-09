from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from diary.forms import PostForm
from diary.models import Post


def tag_detail(request: HttpRequest, tag_name:str) -> HttpResponse:
    qs = Post.objects.all()
    qs = qs.filter(tag_set__name=tag_name)
    return render(request, "diary/tag_detail.html", {"tag_name":tag_name,"post_list":qs},)


def post_list(request: HttpRequest) -> HttpResponse:
    qs = Post.objects.all()
    query = request.GET.get("query","")
    if query:
        qs = qs.filter(title__icontains=query)
    return render(request, "diary/post_list.html", {"post_list": qs})


def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    post = Post.objects.get(pk=pk)
    comment_list = post.comment_set.all()
    tag_list = post.tag_set.all()
    return render(request,"diary/post_detail.html",{
        "post": post, "comment_list": comment_list, "tag_list" : tag_list,
    })


def post_new(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.ip = request.META["REMOTE_ADDR"]
            form.save()
            return redirect("diary:post_list")
    else:
        form = PostForm

    return render(request, "diary/post_form.html", {
        "form": form,
    })


def post_edit(request: HttpRequest, pk: int) -> HttpResponse:
    # 아래 코드는 ModelForm에 한해서 동작하는 코드
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post.save()
            return redirect("diary:post_list")
    else:
        form = PostForm(instance=post)

    return render(request, "diary/post_form.html", {
        "form": form,
    })






	#    def post_new(request: HttpRequest) -> HttpResponse:
 # # print("request.method :", request.method)
 # # print("request.GET :", request.GET) # print("request.POST :", request.POST) # print("request.FILES :", request.FILES) # 입력 서식을 보여주겠다
 # if request.method == "GET":
 # form = PostForm()
 #                #서식 입력값을 전달 받아서 유효성검사를 하겠다
 # # -> 에러 상황에서는 에러 메세지
 # # -> 유효성 검사를 통과하면, 입력값을 보여주고 포스트 리스트로 이동하겠다
 # else:
 # form = PostForm(request.POST, request.FILES)
 #        if form.is_valid():
 # print("유효성검사에 통과했습니다.:", form.cleaned_data)
 #            form.save()   #ModelsForm에서만 사용가능
 # return redirect("diary:post_list")
 #        else:
 # form = PostForm()
 #    return render(request, "diary/post_form.html", {"form":form})