from django.core.validators import MinLengthValidator
from django.db import models

REQUEST_STATUS_CHOICES = [
    ('F', 'FAILED'),
    ('P', 'POSITIVE'),
    ('N', 'NEGATIVE'),
]


# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length=128)
    account_number = models.CharField(
        max_length=10, validators=[MinLengthValidator(10)])

    def __str__(self):
        return f"{self.name} - {self.account_number}"


class Loan(models.Model):
    account = models.ForeignKey(
        to=Account, null=True, on_delete=models.SET_NULL)
    date = models.DateField(auto_now_add=True)
    amount = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.account} - {self.date} - {self.amount}"


class Request(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=REQUEST_STATUS_CHOICES)
