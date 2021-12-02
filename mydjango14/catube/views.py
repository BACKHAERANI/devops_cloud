from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from catube.models import Video
from django.views.generic import ListView


# class based view(CBV)
index = ListView.as_view(model=Video, template_name="catube/index.html")

# Function based view (FBV)
# def index(request: HttpRequest) -> HttpResponse:
#     qs = Video.objects.all()
#     return render(
#         request,
#         "catube/index.html",
#         {"video_list": qs},
#     )


def video_detail(request: HttpRequest, pk=int) -> HttpResponse:
    video = Video.objects.get(pk=pk)
    return render(
        request,
        "catube/video_detail.html",
        {"video": video},
    )
