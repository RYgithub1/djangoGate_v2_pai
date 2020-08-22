from django.db import models


class Article(models.Model):
    # 一行掲示板の作成Article
    # 投稿内容を格納するArticleモデルの定義
    # contentカラムの定義
    content = models.CharField(max_length=200)

    # 名前カラム追加時
    # user_name = models.CharField(max_length=200, null=True)

    # 定義しておけば、マイグレーションによりDBにへデータを投入可能
    def __str__(self):
        return self.content
