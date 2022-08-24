from django.urls import path
from .views import SignInUp, CheckOtp

urlpatterns = [
    path('api/access', SignInUp.as_view()),
    path('api/verify', CheckOtp.as_view()),
]
