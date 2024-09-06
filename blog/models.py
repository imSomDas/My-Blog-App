from django.db import models
from sqlite3 import Timestamp
from datetime import datetime
from django.contrib.auth.models import User
from django.utils.timezone import now 

# Create your models here.
class Post(models.Model):
    Sno = models.AutoField(primary_key=True)
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=50)
    timeStamp = models.DateTimeField(blank=True)
    content = models.TextField()

    def __str__(self):
        return "Posted by "+self.author+" - " + self.title
    

class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default = now)