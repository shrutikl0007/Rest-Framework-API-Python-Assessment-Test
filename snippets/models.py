from django.db import models


class Comment(models.Model):
    title = models.CharField(max_length=255)
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(max_length=100)
    style = models.CharField(max_length=100)

    def __str__(self):
        return self.title
