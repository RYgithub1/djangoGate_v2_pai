# Generated by Django 3.1 on 2020-08-21 13:52

from django.db import migrations, models


# DB変更のための情報を記載、修正。マイグレーションファイル
class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
            ],
        ),
    ]
