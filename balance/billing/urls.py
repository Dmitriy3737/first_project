
from django.urls import path
from .views import CreditView

urlpatterns = [
    path('api/v1/credit/', CreditView.as_view()),
]