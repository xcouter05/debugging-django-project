from django.db import models
from team.models import team

# Create your models here.



class category(models.Model):
    title = models.CharField(max_length=50)
    status = models.BooleanField(default=False)


    def __str__(self):
        return self.title

class tag(models.Model):
    title = models.CharField(max_length=50)
    status = models.BooleanField(default=False)


    def __str__(self):
        return self.title


class blog(models.Model):
    agent = models.ForeignKey(team,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    desc1 = models.TextField()
    desc2 = models.TextField()
    desc3 = models.TextField()
    category = models.ManyToManyField(category)
    tag = models.ManyToManyField(tag)
    img1 = models.ImageField(upload_to='blog', default='default.png')
    img2 = models.ImageField(upload_to='blog', default='default.png')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)


    def __str__(self):
        return self.title
    
    def truncate_chars(self):
        return self.desc1[:20]



class comments(models.Model):
    blog = models.ForeignKey(blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    message = models.TextField()
    post = models.CharField(max_length=50)
    status = models.BooleanField(default=False)


    def __str__(self):
        return self.blog.title
    

class reply(models.Model):
    comment = models.ForeignKey(comments, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    message = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.comment.blog.title




