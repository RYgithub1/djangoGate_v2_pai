from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def indexCity(request):
    # return HttpResponse("city map here")

    context = {
        "messageCity": "city is strong",
        "cityArray": ["月曜日", "火曜日", "水曜日", "木曜日", "金曜日"]
    }
    # renderでテンプレートを呼び出す
    return render(request, 'citymap/indexCity.html', context)
