from django.urls import path# type: ignore
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('activate/<str:uidb64>/<str:token>',views.activate_account,name='activate'),

    # Password reset flow
    path('password-reset/', views.password_reset_view, name='password_reset'),
    path('reset/<uidb64>/<token>/', views.password_reset_confirm_view, name='password_reset_confirm'),
    
]
