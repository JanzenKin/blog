# Generated by Django 3.0.8 on 2020-08-06 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200805_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='isrecommend',
            field=models.BooleanField(default=1, verbose_name='是否推荐'),
            preserve_default=False,
        ),
    ]