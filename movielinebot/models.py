from django.db import models

# Create your models here.

class Movies(models.Model):

    original_title = models.CharField(max_length=30) #片名
    avg_vote = models.CharField(max_length=30) #評分
    director = models.CharField(max_length=50) #導演名稱
    name = models.CharField(max_length=30) #演員名稱
