import random
from django.utils.timezone import now
from datetime import timedelta

from core.models import Client, Admin, CreditScore, Loan, Payment

def create_sample_data():
    sample_names = [
        "Sofia Acosta", "Jensen Reyes", "Audrey Baxter", "Tomas Fischer", "Maci Moody",
        "Ryland Avalos", "Paloma Enriquez", "Elisha Wilkins", "Amalia Patton", "Moises Briggs",
        "Alia Faulkner", "Jabari Lu", "Emani Kirk", "Alessandro Nash", "Novah Cameron",
        "Rayan Thompson", "Madison Gardner", "Alan Walls", "Lilianna Ruiz", "Austin Moody",
        "Elaine Harper", "Hayes Coleman", "Julia Gibbs", "Deacon Carter", "Lucy Bonilla",
        "Aden Middleton", "Madalyn Weaver", "Tucker Villegas", "Jessie Tanner", "Bruno Cross",
        "Nayeli Horton", "Garrett Hendricks", "Dani Hensley", "Layne Palmer", "Juniper Velazquez",
        "Drew Jefferson", "Julieta Guerrero", "Bryce Potter", "Rory Reyna", "Reginald Randolph",
        "Kailey Corona", "Darian Rasmussen", "Esperanza McConnell", "London Potts", "Ellison Hayes",
        "Legend Patel", "Madeline Melton", "Lennon Malone", "Skyler Payne", "Edward Gray",
    ]

    # Create 15 sample Clients
    for name in sample_names[:15]:
        first_name, last_name = name.split()
        Client.objects.create(
            username=f'{first_name.lower()}{last_name.lower()}',
            password='sample_password',
            email=f'{first_name.lower()}.{last_name.lower()}@example.com',
            first_name=first_name,
            last_name=last_name,
            address='Sample Address',
            mobile_number='1234567890',
            occupation='Sample Occupation',
            monthly_income=random.randint(1000, 5000),
            net_worth=random.randint(10000, 50000),
        )

    # Create 5 sample Admins
    for name in sample_names[15:20]:
        first_name, last_name = name.split()
        Admin.objects.create(
            username=f'{first_name.lower()}{last_name.lower()}',
            password='admin_password',
            email=f'{first_name.lower()}.{last_name.lower()}@example.com',
            first_name=first_name,
            last_name=last_name,
            address='Admin Address',
            mobile_number='9876543210',
            salary=random.randint(3000, 8000),
        )

    # Create CreditScore for each Client
    clients = Client.objects.all()
    for client in clients:
        CreditScore.objects.create(
            client_id=client,
            score=random.randint(300, 850),
            date_updated=now(),
            remarks='Sample Remarks',
        )

    # Create 10 sample Loans for the first 10 Clients
    for i, client in enumerate(clients[:10], start=1):
        Loan.objects.create(
            product_name=f'Loan for {client.first_name} {client.last_name}',
            amount=random.randint(1000, 5000),
            interest_rate=random.uniform(1, 10),
            start_date=now().date(),
            end_date=(now() + timedelta(days=random.randint(30, 365))).date(),
            loan_length=0,
            status=random.choice(['Pending', 'Approved', 'Rejected', 'Paid']),
            client_id=client,
            approved_by=None,  # No admin approval yet
        )

    # Create 30 sample Payments for the first 10 Loans
    loans = Loan.objects.all()[:10]
    for loan in loans:
        for _ in range(3):
            Payment.objects.create(
                due_date=now().date(),
                amount=random.randint(50, 200),
                status=random.choice(['Pending', 'Paid']),
                date_paid=now().date(),
                loan_id=loan,
            )

if __name__ == "__main__":
    create_sample_data()
