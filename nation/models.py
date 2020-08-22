from django.db import models


# djangoではこのようにモデル作成 →マイグレーション活用して →mySQLのテーブルを作成
class Nation(models.Model):
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.content
