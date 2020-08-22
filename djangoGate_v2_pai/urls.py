from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # プロジェクト管理のためルーティング２重２箇所変更
    # パス関数う呼び出してurlとbbsを紐付け
    # サーバーアドレスにbbs/が続く場合、bbsアプリケーションのurlsへルート貼る！
    # include関数をここで使うために、上で追記してimport
    path("bbs/", include('bbs.urls')),
    path("citymap/", include("citymap.urls")),

    # nationディレクトリのurlsファイルを利用したい
    path("nation/", include("nation.urls")),
    path('admin/', admin.site.urls),
]
