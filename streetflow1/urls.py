from django .urls import path
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', views.home, name='home'),
    path('login/',auth_views.LoginView.as_view(),name='login'),






    path('password_reset/',auth_views.PasswordResetView. as_view(),name='password_reset'),

    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),

    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

]