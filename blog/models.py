from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()

    def __str__(self):
        # Self hace referencia a la clase Post
        return self.title
