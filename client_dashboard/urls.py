from . import views
from django.urls import path
from django.views.generic import RedirectView

app_name = "client_dashboard"

urlpatterns = [
    path("", views.IndexView.as_view(), name='client_dashboard'),
    path("support/", views.ContactUsView.as_view(), name="support"),
    path("apply/<int:client_id>/", views.ApplyLoanView.as_view(), name="apply"),
]
