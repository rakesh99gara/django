from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self

    def get_absolute_url(self):
        return reverse("showPost", kwargs={"pk": self.pk})
    

    class Meta:  
        db_table = "posts"  


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    comment = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "comments"

class Tag(models.Model):
    tag = models.CharField(max_length=200,unique=True)
    posts = models.ManyToManyField(Post,related_name='tags')

    class Meta:
        db_table = "tags"
# Create your models here.