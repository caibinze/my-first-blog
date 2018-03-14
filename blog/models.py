from django.db import models
from django.utils import timezone

# Create your models here.
# 总是以大写来定义类名
class Post(models.Model):

    # 指向另一个模型的连接
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    
    title = models.CharField(max_length=200) # 有限文本
    text = models.TextField() # 无限文本
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title