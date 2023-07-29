from . import views
from django.urls import path
from django.views.generic import RedirectView

app_name = "dashboard"

urlpatterns = [
    path("", views.IndexView.as_view(), name='dashboard'),
    path("profile/", views.ProfileView.as_view(), name='profile'),
    path("clients/", views.ClientsView.as_view(), name='clients'),
    path("loans/<int:loan_id>/", views.ViewLoanView.as_view(), name='loan'),
    path("loans/approve/<int:loan_id>/", views.ApproveView.as_view(), name="approve"),
    path("loans/reject/<int:loan_id>/", views.RejectView.as_view(), name="reject"),
    path("loans/disapprove/<int:loan_id>/", views.DisapproveView.as_view(), name="disapprove"),
    path("loans/delete/<int:loan_id>/", views.DeleteLoanView.as_view(), name="delete"),
    path("clients/edit/", views.EditProfileClient.as_view(), name="edit"),
    path("clients/<int:user_id>/loans/", views.ClientLoanView.as_view(), name="edit"),
    # create loan resource
    path("loans/create/", views.CreateLoanView.as_view(), name="create"),
    path("payments/", views.PaymentsView.as_view(), name="payments"),

]
