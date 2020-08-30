# Generated by Django 3.0.8 on 2020-08-02 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200802_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.User'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='sort',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Sort'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Article'),
        ),
    ]