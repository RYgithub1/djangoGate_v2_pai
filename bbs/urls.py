# bbs側のルート
from django.urls import path
from . import views


urlpatterns = [
    # ''全体で定義したルーティングに何も追加していなければbbsアプリへ通して、viewsファイルのindex関数を呼び出す
    # nameでこのルートにindexという名前を指定（この名前で関数を呼び出すリンクをはれる）
    path('', views.index, name='index'),
]
