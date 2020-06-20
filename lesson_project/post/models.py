from django.db import models
from django.utils import timezone

CATEGORY = (
    ('', '-----------'),
    ('blog', 'ブログ'),
    ('tweet', 'つぶやき'),
)

class Post(models.Model):
    post_name = models.CharField(verbose_name='投稿者名', max_length=40)
    post_date = models.DateTimeField(verbose_name='投稿日', default=timezone.now)
    category = models.CharField(verbose_name='カテゴリー', max_length=40, blank=False, choices=CATEGORY)
    text = models.TextField(verbose_name='投稿内容')
    is_publish = models.BooleanField(verbose_name='公開フラグ', default=True)