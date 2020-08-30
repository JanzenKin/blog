from django.shortcuts import render, redirect
import logging
from django.conf import settings
from .models import Article, Comments
from .forms import CommentForm

# Create your views here.
logger = logging.getLogger('log')


def global_setting(request):
    return {'SITE_NAME_1': settings.SITE_NAME_1,
            'SITE_NAME_2': settings.SITE_NAME_2,
            }


def index(request):
    try:
        lastest_articles = Article.objects.order_by('-update_time')[:5]
    except Exception as e:
        logger.error(e)

    # 文章存档
    distinct_date_list = Article.objects.distinct_date()
    return render(request, 'index.html',locals())


# 档案
def archive(request):
    try:
        # 先获取客户端提交的信息
        year = request.GET.get('year', None)
        month = request.GET.get('month', None)
        article_list = Article.objects.filter(published_time__icontains=year+'-'+month)
        article_conut = article_list.count
    except Exception as e:
        logger.error(e)
    return render(request, 'archive.html', locals())


def aboutme(request):
    return render(request, 'aboutme.html', locals())


def article(request):
    id = request.GET.get('id', None)
    try:
        article = Article.objects.get(pk=id)
    except Article.DoesNotExist:
        return render(request, 'failure.html', {'reason':'没有找到文章'})
    # 评论表单
    comment_form = CommentForm({'article_id': id})
    # 获取评论信息
    comments = Comments.objects.filter(article=article).order_by('com_id')
    return render(request, 'detail.html', locals())


#提交评论
def comment_post(request):
    try:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            # 获取表单信息
            comment = Comments.objects.create(com_name=comment_form.cleaned_data['com_name'],
                                              com_email=comment_form.cleaned_data['com_email'],
                                              com_content=comment_form.cleaned_data['com_content'],
                                              article_id=comment_form.cleaned_data['article_id'])
            comment.save()
        else:
            return render(request, 'failure.html', {'reason': comment_form.errors})
    except Exception as e:
        logger.error(e)
    return redirect(request.META['HTTP_REFERER'])
