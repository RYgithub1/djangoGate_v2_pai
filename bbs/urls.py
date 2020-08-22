# bbs側のルート
from django.urls import path
from . import views


# railsでshowアクションにも行けるようにルート組むのと同じ。
# ここの行とpath（を通す）の行
# アプリbbsのindexで一覧表示、detailsで詳細表示を、呼び出すpath
app_name = "bbs"


urlpatterns = [
    # ''全体で定義したルーティングに何も追加していなければbbsアプリへ通して、viewsファイルのindex関数を呼び出す
    # nameでこのルートにindexという名前を指定（この名前で関数を呼び出すリンクをはれる）
    path('', views.index, name='index'),
    path('<int:id>', views.detail, name='detail'),
    path('<int:id>', views.delete, name='delete'),
    path('', views.create, name='create')
]
