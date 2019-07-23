from django.db import models


# Create your models here.
class UserProfile(models.Model):
    """
    用户表
    """
    username = models.EmailField(max_length=255, unique=True, )
    password = models.CharField(max_length=128)
