from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from dogtube.models import Video

# Class Based View (CBV)
# index = ListView.as_view(model=Video, template_name="catube/index.html")


# Function Based View (FBV)


def index(request: HttpRequest) -> HttpResponse:
    qs = Video.objects.all()
    return render(request, "dogtube/index.html",{"video_list":qs})


def video_detail(request: HttpRequest, pk=int) ->HttpResponse:
    video= Video.objects.get(pk=pk)
    return render(request,"dogtube/video_detail.html",{"video":video},)