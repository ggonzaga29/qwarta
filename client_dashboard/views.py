from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Sum
from django.shortcuts import render, redirect
from django.views import View
from core.models import User, Client, Payment, Loan, Payment


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


