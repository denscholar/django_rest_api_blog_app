from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.template.defaultfilters import slugify


class Blog(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateField(default=date.today)
    slug = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.name + "==>" + str(self.author)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name + "-" + str(self.created))

        return super().save(*args, **kwargs)

class comment(models.Model):
    body: models.TextField()
    author: models.ForeignKey(User, on_delete=models.SET_NULL)
    commment_date: models.DateTimeField(auto_now_add=True)
    blog: models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.blog.title
    

    
