# Generated by Django 3.0.8 on 2020-08-06 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_article_isrecommend'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='com_headimg',
        ),
    ]
