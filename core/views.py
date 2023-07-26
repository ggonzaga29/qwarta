from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View


class IndexView(View):
    template_name = 'home.html'

    def get(self, request):
        return render(request, self.template_name, {'title': 'Home'})