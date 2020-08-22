# path関数使うので呼び込む
from django.urls import path
# views.を呼び出すので、呼び込む
from . import views


urlpatterns = [
    path("", views.indexNation, name="indexNation")
]
