from . import views
from django.urls import path

app_name = "core"

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
