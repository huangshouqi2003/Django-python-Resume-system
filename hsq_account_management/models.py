from django.db import models

# Create your models here.
class userinfo(models.Model):
    account=models.CharField(max_length=12)
    password = models.CharField(max_length=12)
