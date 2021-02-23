from django.db import models
from django.urls import reverse

# Create your models here.
#title Char
#content Text
#slug unique

class Post(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE, default=1)
    slug = models.SlugField(max_length=300)
    title = models.CharField(max_length=50)
    approvals = models.BooleanField(default=True)
    content = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    