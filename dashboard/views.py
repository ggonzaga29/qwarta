from django.shortcuts import render, redirect
from django.views import View
from core.models import User


class IndexView(View):
    def get(self, request):
        return render(request, "index.html", {})


class ProfileView(View):
    def get(self, request):
        if not request.session["user_id"]:
            return redirect("login")
        else:
            user = User.objects.get(user_id=request.session["user_id"])
            return render(request, "profile.html", {
                "user": user
            })


class LoansView(View):
    def get(self, request):
        return render(request, "loans.html", {})
