from . import views
from django.urls import path
from django.views.generic import RedirectView

app_name = "authentication"

urlpatterns = [
    path("", RedirectView.as_view(url = "/auth/login")),
    path('login', views.LoginView.as_view(), name='login'),
    path('register', views.RegisterView.as_view(), name='register'),
]
