from django.db import models

# Create your models here.


# 自定义文章管理器 1.新增数据处理方法 2.修改原来queryset方法
class ArticleManager(models.Manager):
    def distinct_date(self):
        distinct_date_list = []
        date_list = self.values('published_time')
        for date in date_list:
            date = date['published_time'].strftime('%Y年%m月文章存档')
            if date not in distinct_date_list:
                distinct_date_list.append(date)
        return distinct_date_list


class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='标题', max_length=100,unique=True)
    sort = models.ForeignKey('Sort', to_field='sort_id', on_delete=models.CASCADE)
    abstract = models.CharField(max_length=300, verbose_name='摘要')
    graph = models.ImageField(upload_to = 'avatar/%Y/%m',default='avatar/default.png', max_length=200, verbose_name='图片')
    content = models.TextField(verbose_name='文章内容')
    published_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now_add=True, verbose_name='修改时间')
    likes = models.IntegerField(default=0, verbose_name='喜欢')
    readings = models.IntegerField(default=0, verbose_name='阅读')
    isrecommend = models.BooleanField(verbose_name='是否推荐') # 1推荐 0 不推荐
    flag = models.BooleanField(verbose_name='标记')
    user = models.ForeignKey('User', to_field='uid', on_delete=models.CASCADE)

    objects = ArticleManager()

    class Meta:
        db_table = 'Article'
        verbose_name = '文章'
        verbose_name_plural = '文章'

    def __str__(self):
        return self.title

    # 控制显示长度，必须在adminx的list_display变量中改为函数名
    def short_detail(self):
        if len(str(self.content)) >100:
            return '{}...'.format(str(self.content)[0:99])
        else:
            return str(self.content)

    short_detail.allow_tags = True
    short_detail.short_description = '内容'


class Comments(models.Model):
    com_id = models.AutoField(primary_key=True, verbose_name='ID')
    com_name = models.CharField(max_length=20, verbose_name='评论者名称')
    com_email = models.CharField(max_length=20, verbose_name='邮箱')
    com_pubtime = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    com_content = models.TextField(verbose_name='评论内容')
    con_like = models.IntegerField(default=0, verbose_name='喜欢')
    com_dislike = models.IntegerField(default=0, verbose_name='不喜欢')
    com_flag = models.BooleanField(default=True, verbose_name='标记')
    article = models.ForeignKey('Article', to_field='article_id', on_delete=models.CASCADE)

    class Meta:
        db_table = 'Comments'
        verbose_name = '评论'
        verbose_name_plural = '评论'

    def __str__(self):
        return self.com_name


class Sort(models.Model):
    sort_id = models.AutoField(primary_key=True)
    sort_name = models.CharField(max_length=20, verbose_name='类名')

    class Meta:
        db_table = 'Sort'
        verbose_name = '分类'
        verbose_name_plural = '分类'

    def __str__(self):
        return self.sort_name


class User(models.Model):
    uid = models.AutoField(primary_key=True)
    admin_name = models.CharField(max_length=20, verbose_name='用户名')
    password = models.CharField(max_length=30, verbose_name='密码')
    nickname = models.CharField(max_length=30, verbose_name='昵称')

    class Meta:
        db_table = 'User'
        verbose_name = '用户管理'
        verbose_name_plural = '用户管理'

    def __str__(self):
        return self.nickname