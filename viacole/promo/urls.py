from django.urls import path 
from .views import HomeView, ServicesView, AboutView, LoginView, RegisterView, RegisterConfirmationView, TermsView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('about/', AboutView.as_view(), name="about"),
    path('services/', ServicesView.as_view(), name="services"),
    path('terms/', TermsView.as_view(), name="terms"),
    path('register/', RegisterView.as_view(), name="register"),
    path('register-confirmation/', RegisterConfirmationView.as_view(), name="register-confirmation"),

]
