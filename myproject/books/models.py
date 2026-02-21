from django.db import models

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    year = models.PositiveIntegerField()
    description = models.TextField()
    price = models.PositiveIntegerField()


    def __str__(self):
        return self.title