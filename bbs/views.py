# from django.shortcuts import render
# detailオブジェクトをよびこむため
from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

# モデル(DB)からデータを取り出すのは、viewsの役目ゆえモデル名指定（MVCコントの役目）
from .models import Article


def index(request):
    # return HttpResponse("55! Hello World!")

    articles = Article.objects.all()

    # viewsからtemplatesにデータを渡すにはcontext。
    # {ハッシュ辞書つまりキーバリューの形、受け側viewsはキーで受け取る}
    # contextはrailsのインスタンス変数（キーバリューの形でデータをもつ）
    # context = {"message": "Welcome to BBS jungle"}
    # 渡すのが複数の場合
    context = {
        "message": "Welcome to BBS jungle",
        # "players": ["勇者", "戦士", "魔法使い", " Ninja"]
        'articles': articles,
    }

    # テンプレートを呼び出すのにrender
    # render(データ, テンプレート)。Webページを返すショートカット関数
    # 第三引数にcontextのハッシュ辞書を渡すと、データを渡せるdjango
    return render(request, 'bbs/index.html', context)


# ルートで指定した値をid変数で受ける
def detail(request, id):
    # Articlモデルから実引数idで受けて、対象を変数に代入
    # get_object_or_404指定したidの値を取り出すショートカット関数
    # 404、ページが存在したい場合のエラーメッセージ
    article = get_object_or_404(Article, pk=id)
    # 単純にレスポンスする場合
    # return HttpResponse(article)
    context = {
        "message": "Show Article"+str(id),
        "article": article
    }
    # return render(request, "bbs/index.html", context)
    return render(request, "bbs/detail.html", context)


# ---  検証 ------
# 新規プロフィール、アカウント作成アクション
def create(request):
    article = Article(content='Hello BBS', user_name='eli')
    article.save()

    articles = Article.objects.all()
    context = {
        'message': "Create article",
        'articles': articles,
    }
    return render(request, "bbs/index.html", context)


# 対象の削除アクション
def delete(request, id):
    article = get_object_or_404(Article, pk=id)
    article.delete()

    articles = Article.objects.all()
    context = {
        'message': "Delete Article"+str(id),
        'articles': articles
    }
    return render(request, 'bbs/index.html', context)
