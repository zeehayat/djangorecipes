from django.db import models

# Create your models here.
class Snippet(models.Model):
    title = models.CharField(max_length=100)
    code = models.TextField()
    language = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title