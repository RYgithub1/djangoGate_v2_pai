from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Nation


# Create your views here.0-----
def indexNation(request):
    nations = Nation.objects.all()
    context = {
        "comment": "change it now!",
        "nationCircle": ["赤", "青", "黄", "緑", "紫"],
        "nations": nations,
    }
    # return HttpResponse("united nation")
    return render(request, "nation/indexNation.html", context)


def detail(request, id):
    # pkプライマリキー＝id番号のこと。引数の番号指定など
    nation = get_object_or_404(Nation, pk=id)
    # return HttpResponse(nation)
    context = {
        "speaker": str(id) + "Lets say .. ",
        "nation": nation,
    }
    return render(request, "nation/detailNation.html", context)


def show(request):
    return


def new(request):
    return


def create(request):
    return


def edit(request):
    return


def update(request):
    return


def destroy(request):
    return
