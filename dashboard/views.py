from django.db.models import Sum
from django.shortcuts import render, redirect
from django.views import View
from core.models import User, Client, Payment, Loan, Payment
import datetime


class IndexView(View):
    def get(self, request):
        userCount = Client.objects.count()
        # Sum of payments
        processed_payments = Payment.objects.filter(status="Paid").aggregate(
            total_payments=Sum("amount")
        )
        unprocessed_payments = Payment.objects.filter(status="Pending").aggregate(
            total_payments=Sum("amount")
        )

        loans = Loan.objects.all()

        context = {
            "userCount": userCount,
            "loans": loans,
            "totalPayments": processed_payments["total_payments"],
            "totalUnprocessedPayments": unprocessed_payments["total_payments"]
        }

        return render(request, "dashboard.html", context)


class ProfileView(View):
    def get(self, request):
        if not request.session["user_id"]:
            return redirect("login")
        else:
            user = User.objects.get(user_id=request.session["user_id"])
            return render(request, "profile.html", {"user": user})

    def post(self, request):
        user = User.objects.get(user_id=request.session["user_id"])

        print(user)

        if not user:
            return redirect("login")

        username = request.POST["username"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        address = request.POST["address"]
        mobile_number = request.POST["mobile_number"]
        confirm_password = request.POST["confirm_password"]

        if user.password != confirm_password:
            return render(
                request,
                "profile.html",
                {"error": "Password does not match", "user": user},
            )

        if username != user.username:
            try:
                User.objects.get(username=username)
                return render(
                    request,
                    "profile.html",
                    {"error": "Username already exists", "user": user},
                )
            except User.DoesNotExist:
                user.username = username

        if email != user.email:
            try:
                User.objects.get(email=email)
                return render(
                    request,
                    "profile.html",
                    {"error": "Email already exists", "user": user},
                )
            except User.DoesNotExist:
                user.email = email

        user.first_name = first_name
        user.last_name = last_name
        user.address = address
        user.mobile_number = mobile_number
        user.save()

        return render(
            request,
            "profile.html",
            {"success": "Profile edited successfully!", "user": user},
        )


class LoansView(View):
    def get(self, request):
        return render(request, "clients.html", {})


class ViewLoanView(View):
    def get(self, request, loan_id):
        try:
            loan = Loan.objects.get(loan_id=loan_id)
            payments = Payment.objects.filter(loan_id=loan_id)
            client = Client.objects.get(user_id=loan.client.user_id)

            context = {
                "loan": loan,
                "client": client,
                "payments": payments,
            }

            return render(request, "loan/view_loan.html", context)
        except Loan.DoesNotExist:
            return redirect("/dashboard/")


class ApproveView(View):
    def get(self, request):
        return render(request, "loans.html", {})


class ViewApproveView(View):
    def get(self, request, loan_id):
        try:
            loan = Loan.objects.get(loan_id=loan_id)
            payments = Payment.objects.filter(loan_id=loan_id)
            client = Client.objects.get(user_id=loan.client.user_id)

            context = {
                "loan": loan,
                "client": client,
                "payments": payments,
            }

            loan.status = "Approved"
            loan.start_date = datetime.now().date()

            return render(request, "loans/view_loan.html", context)
        except loan.issue_datet:
            return redirect("/dashboard?")

