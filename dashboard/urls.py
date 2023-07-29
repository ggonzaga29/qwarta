from . import views
from django.urls import path
from django.views.generic import RedirectView

app_name = "dashboard"

urlpatterns = [
    path("", views.IndexView.as_view(), name='dashboard'),
    path("profile/", views.ProfileView.as_view(), name='profile'),
    path("loan/", views.LoansView.as_view(), name='loan'),
    path("loan/<int:loan_id>/", views.ViewLoanView.as_view(), name='loan'),
    path("clients/edit/", views.EditProfileClient.as_view(), name="edit")
]
