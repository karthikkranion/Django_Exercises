from django.urls import path # type: ignore
from . import views



app_name='customer'

urlpatterns = [
   path('dashboard/',views.dashboard_view,name='dashboard'),
   path('change_password/',views.change_password,name='change_password')
   
]
