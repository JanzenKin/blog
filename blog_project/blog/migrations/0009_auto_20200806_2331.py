# Generated by Django 3.0.8 on 2020-08-06 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_remove_comments_com_reply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='com_flag',
            field=models.BooleanField(default=True, verbose_name='标记'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='com_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]