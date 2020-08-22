# path関数使うので呼び込む
from django.urls import path
# views.を呼び出すので、呼び込む
from . import views


app_name = "nation"

urlpatterns = [
    # ビューindexNationアクションから、nameがindexNation.htmlのテンプレートへパスを通す
    path("", views.indexNation, name="indexNation"),

    # path('<int:id>', views.detail, name="detail")
    # ここでパスdetailNationを指定しないと渡せない。
    # 【意味】viewsのdetailアクションから、nameがdetailNation.htmlに、ビューテンプレート間でパス通す
    path('<int:id>', views.detail, name="detailNation")
]
