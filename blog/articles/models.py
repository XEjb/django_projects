from django.db import models
from uuid import uuid4

class Author(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False)
    age = models.IntegerField()
    uuid = models.UUIDField(primary_key=True, default=uuid4)

class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=120, null=False, blank=False)
    content = models.TextField()