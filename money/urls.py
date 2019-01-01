from django.urls import path
from . import views

app_name = 'money'
urlpatterns = [
    path('', views.base_generic, name='base_generic'),
    path('accounts/register_form/', views.register, name='register'),
    path('accounts/register/', views.create_account, name='create_account'),
    path('logged_in/', views.login_view, name='login_view'),
    path('logged_out/', views.logout_view, name='logout_view'),
]