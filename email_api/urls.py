from django.urls import path, include
from . import views

urlpatterns = [
    path('send/', views.SendEmailApiView.as_view(), name='send-email'),
]
