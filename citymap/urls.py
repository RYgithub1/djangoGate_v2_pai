from django.urls import path
from . import views

app_name = "citymap"

# ルーティングはプロジェクト全体と各アプリでの二重、二段階で指定
urlpatterns = [
    path("", views.indexCity, name="indexCity"),
    path("<int:id>", views.detail, name="detail")
]
