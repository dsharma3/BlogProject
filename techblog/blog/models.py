from django.db import models

# Create your models here.
#title Char
#content Text
#slug unique

class Post(models.Model):
    slug = models.SlugField(max_length=300)
    title = models.CharField(max_length=50, unique=True)
    content = models.TextField()

    def __str__(self):
        return self.title