from django.urls import path
from . import views


# ルーティングはプロジェクト全体と各アプリでの二重、二段階で指定
urlpatterns = [
    path("", views.indexCity, name="indexCity"),
]
