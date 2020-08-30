from django.contrib import admin
from .models import *
# Register your models here.


class ArticalAdmin(admin.ModelAdmin):
    list_display = ('title', 'abstract', 'short_detail')
    # fields = ['title', 'abstract', 'content']


    class Media:
        js = (
            '/static/js/kindeditor/kindeditor-all-min.js',
            '/static/js/kindeditor/lang/zh-CN.js',
            '/static/js/kindeditor/config.js',
        )


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('com_id', 'com_name', 'com_content','com_pubtime')


admin.site.register(User)
admin.site.register(Article, ArticalAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(Sort)

