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
    mobile_number = models.CharField(max_length=12)


class Client(User):
    occupation = models.CharField(default='Unemployed', max_length=50)
    monthly_income = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    net_worth = models.DecimalField(default=0, max_digits=10, decimal_places=2)


class Admin(User):
    salary = models.IntegerField(default=0)
    hire_date = models.DateField(default=now)


class CreditScore(models.Model):
    credit_score_id = models.AutoField(primary_key=True)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    score = models.IntegerField()
    date_updated = models.DateField()
    remarks = models.TextField()


# Created through loan application form

class Loan(models.Model):
    loan_id = models.AutoField(primary_key=True)
    # Loan info
    product_name = models.CharField(max_length=255, default='Personal Loan')  # What will you use the money for?
    amount = models.IntegerField(default=0)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)  # 0.00
    start_date = models.DateField()  # date when loan is approved
    end_date = models.DateField()  # date when loan is fully paid
    loan_length = models.IntegerField(default=0)  # in months = end_date - start_date
    issue_date = models.DateField(null=True)  # date when loan is approved
    # Loan status
    status = models.CharField(max_length=50, default='Pending')  # Pending, Approved, Rejected, Paid
    # Foreign keys
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    approved_by = models.ForeignKey(Admin, on_delete=models.CASCADE, default=None, null=True)


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    amount = models.IntegerField(default=0)
    due_date = models.DateField(default=now)
    date_paid = models.DateField(null=True)
    is_late = models.BooleanField(default=False)
    client_id = models.ForeignKey(Client, null=True, on_delete=models.CASCADE)
    loan_id = models.ForeignKey(Loan, null=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default='Pending')  # Pending, Approved, Rejected, Paid

# Other model suggestions:

# - Loan

# - Payment

# - Credit Score

# - Loan Application
