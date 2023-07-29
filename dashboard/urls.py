from . import views
from django.urls import path
from django.views.generic import RedirectView

app_name = "dashboard"

urlpatterns = [
    path("", views.IndexView.as_view(), name='dashboard'),
    path("profile/", views.ProfileView.as_view(), name='profile'),
    path("loans/", views.LoansView.as_view(), name='loans'),
    path("loans/<int:loan_id>/", views.ViewLoanView.as_view(), name='loan'),
]
