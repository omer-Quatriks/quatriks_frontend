from django.urls import path
from django.conf import settings
from .views import AuthView


app_name = 'auth'

urlpatterns = [
    path('signin/', AuthView.as_view(template_name = 'pages/auth/signin.html'), name='signin'),
    path('signup/', AuthView.as_view(template_name = 'pages/auth/signup.html'), name='signup'),
    path('two-factor/', AuthView.as_view(template_name = 'pages/auth/two-factor.html'), name='two-factor'),
    path('new-password/', AuthView.as_view(template_name = 'pages/auth/new-password.html'), name='new-password'),
    path('reset-password/', AuthView.as_view(template_name = 'pages/auth/reset-password.html'), name='reset-password'),
]