from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from django.db.models import Q
from core.models import User, Client, Admin, CreditScore, Loan, Payment
from .seed import generate_clients, generate_admins, generate_credit_scores, generate_loans, generate_payments


class SeedView(View):
    def get(self, request):
        generate_clients(num_clients=5)
        # generate_admins(num_admins=2)
        generate_credit_scores(num_credit_scores=10)
        # generate_loans(num_loans=20)
        # generate_payments()
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

            print(user is Client)
            print(user is Admin)

            if user.user_type == 'client':
                request.session['user_type'] = 'client'
                return redirect('/client')
            elif user.user_type == 'admin':
                request.session['user_type'] = 'admin'
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
