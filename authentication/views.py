from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from django.db.models import Q
from core.models import User

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

            return redirect('/')
        except User.DoesNotExist:
            return render(request, self.template_name, {'title': 'Login', 'error': 'User does not exist'})


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

        if username == '' or password == '' or email == '' or confirm_password == '' or first_name == '' or last_name == '' or mobile_number == '' or address == '':
            print("Error")
            return render(request, self.template_name, {'error': 'Please fill all fields'})

        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            return render(request, self.template_name, {'error': 'User already exists'})

        if password != confirm_password:
            return render(request, self.template_name, {'error': 'Passwords do not match'})

        # create user
        user = User(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name,
            mobile_number=mobile_number,
            address=address
        )

        # save user
        user.save()

        # redirect to login page
        return redirect('/login')


class LogoutView(View):
    def get(self, request):
        request.session.flush()
        return redirect('/login')

