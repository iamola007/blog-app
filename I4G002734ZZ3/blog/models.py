from cgitb import text
from turtle import title
from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE,)
    created_date = models.DateTimeField()
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title
