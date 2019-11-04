from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=11)
    title = models.CharField(max_length=3)
    sex = models.CharField(max_length=6)


class Book(models.Model):
    name = models.CharField(max_length=11)
    number = models.IntegerField()
    author = models.ForeignKey(
        Author,
        related_name='books',
        on_delete=models.CASCADE
    )
