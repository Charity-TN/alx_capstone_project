from django.db import models

# Create your models here.
class Book(models. Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.IntegerField(max_length=13,unique=True)
    published_date = models.DateField()
    copies_available = models.PositiveIntegerField(default=1)

class User(models.Model):
    user_id= models.AutoField(primary_key=True)
    username= models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    date_of_membership = models.DateField(auto_add_now=True)
    active_status = models.BooleanField(default=True)
    check_out_date = models.DateTimeField(default=True)
    return_date = models.DateTimeField(null=True, blank=True)

class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    book= models.ForeignKey(Book, on_delete = models.CASCADE)
    user= models.ForeignKey(User, on_delete = models.CASCADE)
