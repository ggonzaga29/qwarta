from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from django.db.models import Q
from core.models import User, Client, Admin, CreditScore, Loan, Payment
import random
from django.utils.timezone import now
from datetime import timedelta


class SeedView(View):
    def get(self, request):
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
                    amount=random.randint(50000, 100000),
                    status=random.choice(['Pending', 'Paid']),
                    date_paid=now().date(),
                    loan_id=loan,
                )
        return redirect('/')


class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        return render(request, self.template_name, {'title': 'Login'})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        if username == '' or password == '':
            return render(request, self.template_name, {'title': 'Login', 'error': 'Please fill all fields'})

        try:
            user = User.objects.get(Q(username=username) | Q(email=username))

            if user.password != password:
                return render(request, self.template_name, {'title': 'Login', 'error': 'Incorrect password'})

            request.session['user_id'] = user.user_id
            request.session['username'] = user.username
            request.session['email'] = user.email
            request.session['first_name'] = user.first_name
            request.session['last_name'] = user.last_name
            request.session['mobile_number'] = user.mobile_number
            request.session['address'] = user.address

            return redirect('/dashboard')
        except User.DoesNotExist:
            return render(request, self.template_name, {'title': 'Login', 'error': 'User does not exist'})


# Create a new client account
class RegisterView(View):
    template_name = 'register.html'

    def get(self, request):
        return render(request, self.template_name, {'title': 'Register'})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        confirm_password = request.POST['confirm_password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        mobile_number = request.POST['mobile_number']
        address = request.POST['address']
        occupation = request.POST['occupation']
        monthly_income = request.POST['monthly_income']
        net_worth = request.POST['net_worth']

        if username == '' or password == '' or email == '' or confirm_password == '' or first_name == '' or last_name == '' or mobile_number == '' or address == '' or occupation == '' or monthly_income == '' or net_worth == '':
            return render(request, self.template_name, {'error': 'Please fill all fields'})

        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            return render(request, self.template_name, {'error': 'User already exists'})

        if password != confirm_password:
            return render(request, self.template_name, {'error': 'Passwords do not match'})

        # create user
        client = Client()
        client.username = username
        client.password = password
        client.email = email
        client.first_name = first_name
        client.last_name = last_name
        client.mobile_number = mobile_number
        client.address = address
        client.occupation = occupation
        client.monthly_income = monthly_income
        client.net_worth = net_worth

        # save user
        client.save()

        # redirect to login page
        return redirect('/login')


class LogoutView(View):
    def get(self, request):
        request.session.flush()
        return redirect('/login')
