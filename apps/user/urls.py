from django.urls import path

from .api_endpoints import *

app_name = 'user'

urlpatterns = [
    path('register/', RegisterApi.as_view(), name='register'),
    path('login/', LoginApi.as_view(), name='login'),
    path('forgot-password/', ForgotPasswordApi.as_view(), name='forgot-password'),
    path('reset-password/', ResetPasswordApi.as_view(), name='reset-password')    
]
