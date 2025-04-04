from django.db import models
from django.utils.timezone import now
from datetime import timedelta

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

class tracking(models.Model):
    tracking_id = models.AutoField(primary_key = True)
    transaction = models.OnetoOne(Transaction, on_delete = models.CASCADE)
    days_overdue = models.IntegerField(default=0)
    resolved = models.BooleanField(default=False)
    penalty_amount = models.DefaultField(max_digits =10, decimal_places = 2, default = 0.00)

    def calculate_overdue_days(self):
        """Calculate overdue days based on the due date from the transaction."""
        if self.transaction.return_date:
            return 0  # No overdue if returned on time
        overdue_days = (now().date() - self.transaction.check_out_date.date()).days - 14  # Assuming 14-day loan period
        return max(overdue_days, 0)  # Ensure no negative values

    def save(self, *args, **kwargs):
        """Automatically update days overdue before saving."""
        self.days_overdue = self.calculate_overdue_days()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Tracking ID: {self.tracking_id}, Overdue: {self.days_overdue} days"


