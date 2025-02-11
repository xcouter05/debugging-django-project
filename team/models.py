from django.db import models

# Create your models here.


class skill(models.Model):
    skill = models.CharField(max_length=30)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.skill
    

class team(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='team', default='default.png')
    skill = models.ManyToManyField(skill)
    content = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name