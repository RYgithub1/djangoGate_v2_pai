from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def indexNation(request):
    context = {
        "comment": "change it now!",
        "nationCircle": ["赤", "青", "黄", "緑", "紫"]
    }
    # return HttpResponse("united nation")
    return render(request, "nation/indexNation.html", context)


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
