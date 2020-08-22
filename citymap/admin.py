from django.contrib import admin

# マイグレファイル0001_initial.pyの、nameに登録するテーブル名指定、これに合わせて、 Introductionを登録register
from .models import Introduction
# from .models import Article

# Register your models here.
admin.site.register(Introduction)
# admin.site.register(Article)
