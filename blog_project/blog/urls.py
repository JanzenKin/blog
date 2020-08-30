from django.urls import path
from blog.views import index, archive, aboutme, article, comment_post

urlpatterns = [
    path('', index, name='index'),
    path('archive/', archive, name="archive"),
    path('aboutme/', aboutme, name="aboutme"),
    path('detail/', article, name="detail"),
    path('comment/post', comment_post,  name="comment_post"),
]
