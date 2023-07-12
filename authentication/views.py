from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View


class IndexView(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name, {'title': 'Home'})


class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        return render(request, self.template_name, {'title': 'Login'})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']


class RegisterView(View):
    template_name = 'register.html'

    def get(self, request):
        return render(request, self.template_name, {'title': 'Register'})
