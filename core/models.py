from django.db import models


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=11)


class Client(User):
    salary = models.IntegerField()
    type = models.CharField(max_length=10)


class Admin(User):
    type = models.CharField(max_length=10)


class Loan(models.Model):
    loan_id = models.AutoField(primary_key=True)
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
    transaction_id = models.AutoField(primary_key=True)
    transaction_date = models.DateField()
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    admin_id = models.ForeignKey(Admin, on_delete=models.CASCADE)


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    amount = models.IntegerField()
    payment_date = models.DateField()
    loanid = models.ForeignKey(Loan, on_delete=models.CASCADE)