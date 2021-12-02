from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from catube.models import Video


def index(request: HttpRequest) -> HttpResponse:
    qs = Video.objects.all()
    return render(
        request,
        "catube/index.html",
        {"video_list": qs},
    )


def video_detail(request: HttpRequest, pk=int) -> HttpResponse:
    video = Video.objects.get(pk=pk)
    return render(
        request,
        "catube/video_detail.html",
        {"video": video},
    )
