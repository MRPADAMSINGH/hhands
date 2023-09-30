from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('subscribe', views.subscribe, name='subscribe'),
    path("register", views.register, name="register"),
    path('login', views.custom_login, name='login'),
    path('logout', views.custom_logout, name='logout'),
    path('profile/<username>', views.profile, name='profile'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    # path("password_change", views.password_change, name="password_change"),
    path("password_reset", views.password_reset_request, name="password_reset"),
    path('reset/<uidb64>/<token>', views.passwordResetConfirm, name='password_reset_confirm'),
    # path('login', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    # path('logout', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]