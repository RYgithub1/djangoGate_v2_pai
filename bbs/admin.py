# 管理者アカウントadminで操作
from django.contrib import admin

# モデル経由でArticleテーブル作成
from .models import Article
# from .models import Prof


# モデル経由で、bbsの、Articlsテーブル作成（管理画面に表出）
admin.site.register(Article)
# admin.site.register(Prof)
