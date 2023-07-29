from . import views
from django.urls import path
from django.views.generic import RedirectView

app_name = "client_dashboard"

urlpatterns = [
    path("", views.IndexView.as_view(), name='client_dashboard'),
]