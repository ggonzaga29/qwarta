from django.db import models


class User(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    mobilenumber = models.CharField(max_length=10)


class Client(User):
    salary = models.IntegerField()
    type = models.CharField(max_length=10)


class Admin(User):
    type = models.CharField(max_length=10)


class Loan(models.Model):
    loanid = models.AutoField(primary_key=True)
    amount = models.IntegerField()
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=10)
    description = models.TextField()
    terms = models.IntegerField()
    release_date = models.DateField()
    clientid = models.ForeignKey(Client, on_delete=models.CASCADE)


class TransactionReport(models.Model):
    transactionid = models.AutoField(primary_key=True)
    transaction_date = models.DateField()
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    admin_id = models.ForeignKey(Admin, on_delete=models.CASCADE)


class Payment(models.Model):
    paymentid = models.AutoField(primary_key=True)
    amount = models.IntegerField()
    payment_date = models.DateField()
    loanid = models.ForeignKey(Loan, on_delete=models.CASCADE)