from django.db import models
from django.utils.timezone import now

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
    occupation = models.CharField(default='Unemployed', max_length=50)
    monthly_income = models.IntegerField(default=0)
    monthly_expenses = models.IntegerField(default=0)
    
    
class CreditScore(models.Model):
    score_id = models.AutoField(primary_key=True)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    score = models.IntegerField()
    date_updated = models.DateField()
    remarks = models.TextField()


class Admin(User):
    salary = models.IntegerField(default=0)
    hire_date = models.DateField(default=now)
    

class Loan(models.Model):
    loan_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255, default='Personal Loan')
    amount = models.IntegerField(default=0)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=10)
    description = models.TextField()
    terms = models.IntegerField()
    release_date = models.DateField()
    issue_date = models.DateField(default=now)
    issued_by = models.ForeignKey(Admin, on_delete=models.CASCADE, default=1)
    is_approved = models.BooleanField(default=False)
    clientid = models.ForeignKey(Client, on_delete=models.CASCADE)


class TransactionReport(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    amount = models.IntegerField(default=0)
    transaction_date = models.DateField()
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    admin_id = models.ForeignKey(Admin, on_delete=models.CASCADE)
    

class ClientDocument(models.Model):
    document_id = models.AutoField(primary_key=True)
    document_name = models.CharField(max_length=50)
    document_type = models.CharField(max_length=50)
    document_date = models.DateField()
    clientid = models.ForeignKey(Client, on_delete=models.CASCADE)
    adminid = models.ForeignKey(Admin, on_delete=models.CASCADE)
    loanid = models.ForeignKey(Loan, on_delete=models.CASCADE)


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    amount = models.IntegerField()
    payment_date = models.DateField()
    loanid = models.ForeignKey(Loan, on_delete=models.CASCADE)
    

