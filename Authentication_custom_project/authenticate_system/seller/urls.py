from django.urls import path # type: ignore
from . import views

app_name='seller'
urlpatterns = [
   path('',views.seller_dashboard,name='seller_dashboard')
]
