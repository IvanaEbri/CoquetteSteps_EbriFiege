from django.urls import path
from .views import CustomLoginView, CustomLogoutView, RegistrationView, LogoutConfirmationView

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("register/", RegistrationView.as_view(), name="register"),
    path("confirm_logout/", LogoutConfirmationView.as_view(), name="confirm_logout"),
]