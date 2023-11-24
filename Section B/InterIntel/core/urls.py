from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="homepage"),
    path("register/", views.register_request, name="registerPage"),
    path("login/", views.login_request, name='loginPage'),
    path("logout/", views.logout_request, name='logout'),
    path("success/", views.success_view, name="success")

]