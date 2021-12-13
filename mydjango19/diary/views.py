from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from diary.forms import PostForm, CommentForm
from diary.models import Post, Comment


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
    post = get_object_or_404(Post, pk=pk)

                                                                                        # try:
                                                                                        #     post = Post.objects.get(pk=pk)
                                                                                        # except Post.DoesNotExist:
                                                                      #     raise Http404
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
            messages.success(request, "성공적")
            return redirect("diary:post_list")
    else:
        form = PostForm

    return render(request, "diary/post_form.html", {
        "form": form,
    })


def post_edit(request: HttpRequest, pk: int) -> HttpResponse:
    post = get_object_or_404(Post, pk=pk)
    # 아래 코드는 ModelForm에 한해서 동작하는 코드
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post.save()
            messages.success(request, "성공적으로 수정되었습니다.")
            return redirect("diary:post_list")
    else:
        form = PostForm(instance=post)

    return render(request, "diary/post_form.html", {
        "form": form,
    })


def comment_new(request: HttpRequest, post_pk: int) -> HttpResponse:
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)   #전달받은 인자에 대한 유효성 검사와 에러 출력/ 정보는 form이 알고 있다
        if form.is_valid():
                                               # form.cleaned_data  #유효성 검사에 통과한 값들(dict)
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect("diary:post_detail", post_pk)
    else:
        form = CommentForm()
    return render(request, "diary/comment_form.html", {"form": form})


def comment_edit(request: HttpRequest, post_pk: int, pk: int) -> HttpResponse:
    comment = get_object_or_404(Comment, pk=pk)

    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            comment.save()
            messages.success(request, "성공적으로 수정되었습니다.")
            return redirect("diary:post_detail", post_pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, "diary/comment_form.html", {"form": form})






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