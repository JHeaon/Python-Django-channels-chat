from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    
    class Meta:
        ordering = ["-id"] # 쿼리셋의 디폴트 정렬