from . import views
from django.urls import path
from django.views.generic import RedirectView

app_name = "client_dashboard"

urlpatterns = [
    path("", views.IndexView.as_view(), name='client_dashboard'),
    path("support/", views.ContactUsView.as_view(), name="support"),
    path("apply/", views.ApplyLoanView.as_view(), name="apply"),
    path("pay/<int:payment_id>", views.PaymentView.as_view(), name="pay"),
    path("loan/<int:loan_id>/", views.ViewLoanView.as_view(), name='loan'),
]
