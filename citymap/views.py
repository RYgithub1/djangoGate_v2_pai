from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Introduction

# Create your views here.


def indexCity(request):
    # return HttpResponse("city map here")

    introductions = Introduction.objects.all()

    context = {
        "messageCity": "city is strong",
        "cityArray": ["月曜日", "火曜日", "水曜日", "木曜日", "金曜日"],
        "introductions": introductions,
    }
    # renderでテンプレートを呼び出す
    return render(request, 'citymap/indexCity.html', context)


def detail(request, id):
    introduction = get_object_or_404(Introduction, pk=id)
    # return HttpResponse(introduction)

    context = {
        "message": str(id) + "Introductionでっせ",
        "introduction": introduction
    }
    return render(request, "citymap/detail.html", context)
