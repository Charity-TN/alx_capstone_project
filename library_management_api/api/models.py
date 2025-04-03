from django.db import models

# Create your models here.
class Book(models. Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.IntegerField(max_length=13,unique=True)
    published_date = models.DateField()
    copies_available = models.PositiveIntegerField(default=1)
