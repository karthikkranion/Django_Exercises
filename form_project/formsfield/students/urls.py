from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('candidate/<int:candidate_id>/',views.candidate_detail,name='candidate_detail'),
]
