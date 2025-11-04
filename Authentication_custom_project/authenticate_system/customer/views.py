from django.contrib import messages # type: ignore
from django.shortcuts import render # type: ignore
from django.contrib.auth.forms import PasswordChangeForm # type: ignore
from django.shortcuts import redirect  # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from django.contrib.auth import logout,update_session_auth_hash # type: ignore
from authenticate_system.decorators import login_and_user_required
# Create your views here.
@login_and_user_required('customer')
def dashboard_view(request):
    return render(request,'customer/dashboard.html')

@login_and_user_required('customer')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # keeps session valid
            logout(request)
            messages.success(request, 'Password changed successfully! Please log in again.')
            return redirect('login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, 'customer/password_change.html', {'form': form})
