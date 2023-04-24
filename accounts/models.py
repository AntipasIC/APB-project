from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()

class Customerbalance(models.Model):
    #table for student account balance
    parkCustomer = models.ForeignKey(User,on_delete = models.CASCADE)
    balance = models.FloatField(default=0)
    transactionType = models.CharField(default="deposit",max_length=50)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.balance)



class Transactions(models.Model):
    #table for transactions made by parking customer
    parkCustomer = models.ForeignKey(User,on_delete = models.CASCADE)
    transactionId = models.CharField(max_length=50,primary_key=True)
    transactionTime = models.DateTimeField(auto_now_add=True)
    transactionType = models.CharField(max_length=50)
    amount = models.FloatField()
    balance = models.OneToOneField(Customerbalance, on_delete = models.SET_DEFAULT,default=0)

    def __str__(self):
        return self.transactionid


class PaynowPayment(models.Model):
    #table for paynow payments made by student
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    cellphone = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    reference = models.CharField(max_length=100)
    paynow_reference = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    #details = models.CharField(max_length=500, blank=True)

    init_status = models.CharField(max_length=10, blank=True)
    poll_url = models.CharField(max_length=500)
    browser_url = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10)
    paid = models.BooleanField(default=False)
    confirmed_at = models.DateTimeField(null=True, blank=True)
    balance = models.OneToOneField(Customerbalance,on_delete = models.SET_DEFAULT,default=0)

    def __str__(self):
        return self.user.username + ' - $' + str(self.amount) + ' - ' + self.status
