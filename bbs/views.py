from django.shortcuts import render
from django.http import HttpResponse

# モデル(DB)からデータを取り出すのは、viewsの役目ゆえ（MVCコントの役目）


def index(request):
    # return HttpResponse("55! Hello World!")

    # viewsからtemplatesにデータを渡すにはcontext。
    # {ハッシュ辞書つまりキーバリューの形、受け側viewsはキーで受け取る}
    # contextはrailsのインスタンス変数（キーバリューの形でデータをもつ）
    # context = {"message": "Welcome to BBS jungle"}
    # 渡すのが複数の場合
    context = {
        "message": "Welcome to BBS jungle",
        "players": ["勇者", "戦士", "魔法使い", " Ninja"]
    }

    # テンプレートを呼び出すのにrender
    # render(データ, テンプレート)。Webページを返すショートカット関数
    # 第三引数にcontextのハッシュ辞書を渡すと、データを渡せるdjango
    return render(request, 'bbs/index.html', context)
