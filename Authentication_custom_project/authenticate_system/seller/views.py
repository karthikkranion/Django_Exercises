from django.shortcuts import render # type: ignore
from authenticate_system.decorators import login_and_user_required

# Create your views here.
@login_and_user_required('seller')
def seller_dashboard(request):
    return render(request,'seller/dashboard.html')