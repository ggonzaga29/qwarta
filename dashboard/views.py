from django.db.models import Sum
from django.shortcuts import render, redirect
from django.views import View
from django.utils.timezone import timedelta
from core.models import User, Client, Payment, Loan, Payment, CreditScore
from datetime import datetime


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

            # payments = list(payments).sort(key=lambda r: r.due_date)

            current_outstanding = 0
            for p in payments:
                if p.status == "Pending":
                    print(p.status)
                    current_outstanding += p.amount
                    print(current_outstanding)

            context = {
                "loan": loan,
                "client": client,
                "payments": payments,
                "current_outstanding": current_outstanding
            }

            return render(request, "loan/view_loan.html", context)
        except Loan.DoesNotExist:
            return redirect("/dashboard/")


class ApproveView(View):
    def get(self, request, loan_id):
        loan = Loan.objects.get(loan_id=loan_id)

        if loan.status == "Approved":
            return redirect("/dashboard/loans/" + str(loan_id))

        loan.status = "Approved"
        loan.issue_date = datetime.today()
        loan.save()

        current_date = loan.start_date
        for _ in range(loan.loan_length + 1):
            amount = (loan.amount_to_pay // loan.loan_length)
            due_date = current_date + timedelta(days=30)
            status = "Pending"
            is_late = False

            payment = Payment(
                amount=amount,
                due_date=due_date,
                status=status,
                is_late=is_late,
                client_id=loan.client,
                loan_id=loan,
            )

            payment.save()
            print(payment)
            current_date += timedelta(days=30)

        return redirect("/dashboard/loans/" + str(loan_id))


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

            loan.status = 'Approve'
            loan.issue_date = datetime.now()

            return render(request, "loans/view_loan.html", context)
        except Loan.DoesNotExist:
            return redirect("/dashboard?")


class ClientsView(View):
    def get(self, request):
        clients = Client.objects.all()

        for client in clients:
            creditScore = CreditScore.objects.get(client_id=client.user_id)
            client.creditScore = creditScore

        context = {
            "clients": clients,
        }
        return render(request, "clients.html", context)

    def post(self, request):
        user_id = request.POST["client_user_id"]
        username = request.POST["client_username"]
        email = request.POST["client_email"]
        first_name = request.POST["client_first_name"]
        last_name = request.POST["client_last_name"]
        address = request.POST["client_address"]
        mobile_number = request.POST["client_mobile_number"]
        occupation = request.POST["client_occupation"]
        monthly_income = request.POST["client_monthly_income"]
        net_worth = request.POST["client_net_worth"]

        client = Client.objects.get(user_id=user_id)
        client.username = username
        client.email = email
        client.first_name = first_name
        client.last_name = last_name
        client.address = address
        client.mobile_number = mobile_number
        client.occupation = occupation
        client.monthly_income = monthly_income
        client.net_worth = net_worth

        client.save()

        return redirect(request.META.get('HTTP_REFERER'))


class PaymentsView(View):
    def get(self, request):
        status_param = request.GET.get("status", "Paid")
        payments = Payment.objects.filter(status=status_param)
        for payment in payments:
            client = Client.objects.get(user_id=payment.client_id.user_id)
            payment.client = client
            loan = Loan.objects.get(loan_id=payment.loan_id.loan_id)
            payment.loan = loan

        context = {
            "payments": payments,
        }
        return render(request, "payments.html", context)


class ClientLoanView(View):
    def get(self, request, user_id):
        loans = Loan.objects.filter(client_id=user_id)
        client = Client.objects.get(user_id=user_id)
        context = {
            "loans": loans,
            "client": client,
        }
        return render(request, "client_loans.html", context)


class DeleteLoanView(View):
    def get(self, request, loan_id):
        loan = Loan.objects.get(loan_id=loan_id)
        loan.delete()
        return redirect(request.META.get('HTTP_REFERER'))


class EditProfileClient(View):
    def post(self, request):
        client = Client.objects.get(user_id=request.POST["user_id"])

        client.address = request.POST["client_address"]
        client.occupation = request.POST["client_occupation"]
        client.monthly_income = request.POST["client_monthly_income"]
        client.net_worth = request.POST["client_net_worth"]
        client.mobile_number = request.POST["client_mobile_number"]
        print(client.address)

        client.save()

        return redirect(request.META.get('HTTP_REFERER'))
