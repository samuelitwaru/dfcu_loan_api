from django.core.validators import MinLengthValidator
from django.db import models


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=128)
    account_number = models.CharField(max_length=10, validators=[MinLengthValidator(10)])

    def __str__(self):
        return self.name


class Loan(models.Model):
    customer = models.ForeignKey(to=Customer, null=True, on_delete=models.SET_NULL)
    date = models.DateField(auto_now_add=True)
    amount = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.date} - {self.amount}"
    
