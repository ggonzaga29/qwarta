from . import views
from django.urls import path
from django.views.generic import RedirectView
from .views import ContactUsView


app_name = "client_dashboard"

urlpatterns = [
    path("", views.IndexView.as_view(), name='client_dashboard'),
    path('contact/', ContactUsView.as_view(), name='contact_us'),
    path("client/<int:loan_id>/", views.ViewLoanView.as_view(), name='loan'),
]