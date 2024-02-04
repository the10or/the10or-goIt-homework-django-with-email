from django.db import models


# Create your models here.


class Author(models.Model):
    fullname = models.CharField(max_length=100, unique=True)
    born_date = models.CharField(max_length=100)
    born_location = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.fullname


class Quote(models.Model):
    text = models.TextField()
    author = models.ForeignKey(
        Author, null=True, on_delete=models.CASCADE, default=None
    )
    tags = models.ManyToManyField("Tag")


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
