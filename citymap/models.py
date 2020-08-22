
from django.db import models


# djangoではこのようにモデル作成 →マイグレーション活用して →mySQLのテーブルを作成
class Introduction(models.Model):
    # プロフィールのDBの作成Introduction
    # 投稿内容を格納するIntroductionモデルの定義
    # contentカラムの定義
    content = models.CharField(max_length=200)

    # 定義しておけば、マイグレーションによりDBにへデータを投入可能
    def __str__(self):
        return self.content
