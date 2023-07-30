import random
from faker import Faker
from django.utils.timezone import timedelta
from django.utils.timezone import now
from core.models import User, Client, Admin, CreditScore, Loan, Payment

fake = Faker()

loan_names = [
    "Personal Loan",
    "Home Loan",
    "Auto Loan",
    "Business Loan",
    "Education Loan",
    "Medical Loan",
    "Vacation Loan",
    "Wedding Loan",
    "Debt Consolidation Loan",
    "Emergency Loan",
    "Renovation Loan",
    "Travel Loan",
    "Technology Loan",
    "Green Loan",
    "Holiday Loan",
    "Car Repair Loan",
    "Furniture Loan",
    "Appliance Loan",
    "Short-term Loan",
    "Long-term Loan",
    "Payday Loan",
    "Microloan",
    "Peer-to-Peer Loan",
    "Installment Loan",
    "Secured Loan",
    "Unsecured Loan",
    "Credit Card Loan",
    "Student Loan",
    "Medical Expense Loan",
    "Home Improvement Loan",
    "Mortgage Loan",
    "Small Business Loan",
    "Equipment Loan",
    "Revolving Loan",
    "Bridge Loan",
    "Consolidation Loan",
    "Refinance Loan",
    "Personal Line of Credit",
    "Business Line of Credit",
]


# Generate random clients
def generate_clients(num_clients):
    clients = []
    for _ in range(num_clients):
        client = Client(
            username=fake.user_name(),
            password=fake.password(),
            email=fake.email(),
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            address=fake.address(),
            mobile_number=fake.phone_number(),
            occupation=fake.job(),
            monthly_income=random.randint(1000, 10000),
            net_worth=random.randint(10000, 100000)
        )
        clients.append(client)

    for client in clients:
        client.save()


# Generate random admins
def generate_admins(num_admins):
    admins = []
    for _ in range(num_admins):
        admin = Admin(
            username=fake.user_name(),
            password=fake.password(),
            email=fake.email(),
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            address=fake.address(),
            mobile_number="0000000",
            salary=random.randint(50000, 100000),
            hire_date=fake.date_between(start_date='-5y', end_date='today')
        )
        admins.append(admin)

    for admin in admins:
        admin.save()


# Generate random credit scores for clients
def generate_credit_scores(num_credit_scores):
    credit_scores = []
    clients = Client.objects.all()

    for client in clients:
        credit_score = CreditScore(
            client_id=client,
            score=random.randint(300, 850),
            date_updated=fake.date_between(start_date='-1y', end_date='today'),
            remarks=fake.text()
        )
        credit_scores.append(credit_score)

    for credit_score in credit_scores:
        credit_score.save()


# Generate random loans for clients
def generate_loans(num_loans):
    loans = []
    clients = Client.objects.all()
    for _ in range(num_loans):
        client = random.choice(clients)
        start_date = fake.date_between(start_date='-1y', end_date='today')
        end_date = start_date + timedelta(days=random.randint(30, 365) * 12)  # Loan length between 1 and 12 months
        status = random.choice(['Pending', 'Approved', 'Rejected'])
        loan_length = (end_date - start_date).days // 30
        amount = random.randint(1000, 50000)
        interest_rate = random.uniform(5.0, 15.0)

        loan = Loan(
            product_name=random.choice(loan_names),
            amount=amount,
            interest_rate=interest_rate,
            start_date=start_date,
            end_date=end_date,
            amount_to_pay=amount + (amount * (interest_rate / 100) * (loan_length / 12)),
            # loan length in months
            loan_length=(end_date - start_date).days // 30,
            status=status,
            #  if loan is approved, issue date is 7 days before start date
            issue_date=start_date - timedelta(days=7) if status == 'Approved' else None,
            client_id=client.user_id
        )
        loans.append(loan)

    for loan in loans:
        loan.save()


# Generate random payments for loans
# class Payment(models.Model):
#     payment_id = models.AutoField(primary_key=True)
#     amount = models.IntegerField()
#     due_date = models.DateField(default=now)
#     date_paid = models.DateField()
#     is_late = models.BooleanField(default=False)
#     client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
#     loan_id = models.ForeignKey(Loan, on_delete=models.CASCADE)
#     status = models.CharField(max_length=50, default='Pending')  # Pending
def generate_payments():
    payments = []
    loans = Loan.objects.filter(status='Approved')
    for loan in loans:
        current_date = loan.start_date
        for i in range(loan.loan_length + 1):
            # due date is 30 days after start date
            # multiplied by interest rate
            amount = (loan.amount_to_pay // loan.loan_length)
            due_date = current_date + timedelta(days=30)
            status = random.choice(['Pending', 'Paid'])
            is_late = random.choice([True, False]) if status == 'Paid' else False
            # if is late, date paid is 7 days after due date
            date_paid = due_date + timedelta(days=7) if is_late else due_date - timedelta(days=random.randint(0, 7))

            payment = Payment(
                amount=amount,
                due_date=due_date,
                date_paid=date_paid,
                is_late=is_late,
                client_id=loan.client,
                loan_id=loan,
                status=status
            )
            payments.append(payment)
            current_date += timedelta(days=30)

    for payment in payments:
        payment.save()
