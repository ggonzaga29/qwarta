from datetime import datetime

from django.db.models import Sum
from django.shortcuts import render, redirect
from django.views import View

from core.models import Client, Payment, Loan, CreditScore


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

        # Fetch loans belonging to the current user
        client = Client.objects.get(user_id=request.session.get('user_id'))
        loans = Loan.objects.filter(client=client)

        context = {
            "userCount": userCount,
            "loans": loans,
            "totalPayments": processed_payments["total_payments"],
            "totalUnprocessedPayments": unprocessed_payments["total_payments"]
        }

        return render(request, "client_dashboard.html", context)


class ContactUsView(View):
    def get(self, request):
        return render(request, 'Contact_Us.html')


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
            return redirect("/client_dashboard/")




class ApplyLoanView(View):
    def get(self, request, client_id):
        user_id = request.session["user_id"]
        start_date = request.GET.get("start_date", None)
        end_date = request.GET.get("end_date", None)
        amount = request.GET.get("amount", None)
        product_name = request.GET.get("product_name", None)

        clients = Client.objects.get(user_id=request.session["user_id"])

        loan_length = 0

        context = {
            "clients": clients,
        }

        if user_id:
            context["user_id"] = int(user_id)
            client = Client.objects.get(user_id=user_id)
            context["client"] = client
            credit = CreditScore.objects.get(client_id=user_id)
            context["credit"] = credit

            if credit.score > 700:
                context["interest"] = 7
            elif credit.score > 500:
                context["interest"] = 10
            elif credit.score > 400:
                context["interest"] = 12
            elif credit.score > 300:
                context["interest"] = 15

        if product_name:
            context["product_name"] = product_name

        if start_date:
            context["start_date"] = start_date

        if end_date:
            context["end_date"] = end_date

        if start_date and end_date:
            # dd/mm/YY
            start_date = datetime.strptime(start_date, "%Y-%m-%d")
            end_date = datetime.strptime(end_date, "%Y-%m-%d")
            loan_length = (end_date - start_date).days // 30
            context["loan_length"] = loan_length

        if amount:
            context["amount"] = amount
            context["amount_to_pay"] = int(amount) + (int(amount) * (context["interest"] / 100) * (loan_length / 12))

        return render(request, "client_apply.html", context)

    def post(self, request, client_id):
        user_id = request.POST["user_id"]
        start_date = request.POST["start_date"]
        end_date = request.POST["end_date"]
        product_name = request.POST["product_name"]
        loan_length = request.POST["loan_length"]
        amount = request.POST["amount"]
        amount_to_pay = request.POST["amount_to_pay"]
        interest = request.POST["interest"]

        loan = Loan(
            client_id=user_id,
            product_name=product_name,
            start_date=start_date,
            end_date=end_date,
            amount=amount,
            amount_to_pay=float(amount_to_pay),
            loan_length=loan_length,
            interest_rate=interest,
            status="Pending",
        )

        loan.save()
        print(loan)

        return redirect("/client" + str(loan.loan_id))
