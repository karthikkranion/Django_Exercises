from django.shortcuts import render, redirect # type: ignore
from django.urls import reverse# type: ignore
from .models import User
from account.forms import RegistrationForm
from django.contrib.auth.forms import PasswordResetForm,SetPasswordForm  # type: ignore
from django.contrib import messages# type: ignore
from django.conf import settings# type: ignore
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode# type: ignore
from django.utils.encoding import force_bytes, force_str# type: ignore
from django.contrib.auth.tokens import default_token_generator# type: ignore
from account.utils import send_activation_email,reset_password_email
from django.contrib.auth import authenticate,login,logout # type: ignore
from authenticate_system.utils import add_permission

def home_view(request):
    return render(request, 'account/home.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect(
            'seller:seller_dashboard' if request.user.is_seller 
            else 'customer:dashboard' if request.user.is_customer 
            else 'home'
        )

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not (email and password):
            messages.error(request, 'Both fields are required')
            return redirect('login')

        user = authenticate(request, username=email, password=password)

        if not user:
            messages.error(request, 'Invalid email or password')
        elif not user.is_active:
            messages.error(request, 'User is not activated')
        else:
            login(request, user)
            return redirect(
                'customer:dashboard' if user.is_customer 
                else 'seller:seller_dashboard' if user.is_seller 
                else 'home'
            )

        return redirect('login')

    return render(request, 'account/login.html')

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.is_active = False
            
            role=form.cleaned_data.get('role')
            if role == 'seller':
                user.is_seller =True
                user.is_customer=False
            else:
                user.is_seller =False
                user.is_customer=True

              
            user.save()  # This creates a valid PK!
            add_permission(role,user)

            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            activation_link = reverse('activate', kwargs={'uidb64': uidb64, 'token': token})
            activation_url = f'{settings.SITE_DOMAIN}{activation_link}'
            
            # Debug print
            print("RegisterView: user.pk", user.pk)
            print("RegisterView: uidb64", uidb64)
            print("RegisterView: activation_url", activation_url)
            
            send_activation_email(user.email, activation_url)
            messages.success(request, 'User registered successfully! Please check your email to activate your account.')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = RegistrationForm()
    
    return render(request, 'account/register.html', {'form': form})

def activate_account(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        print("ActivateAccount: uidb64", uidb64)
        print("ActivateAccount: decoded uid", uid)
        user = User.objects.get(pk=uid)
        
        if user.is_active:
            messages.warning(request, 'This account has already been activated.')
            return redirect('login')
        
        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(request, 'Your account has been activated successfully! You can now log in.')
            return redirect('login')
        else:
            messages.error(request, 'Activation link is invalid or expired! Please register again or request a new activation link.')
            return redirect('login')
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        messages.error(request, "Activation link invalid or user not found. Please register again.")
        return redirect('login')

def password_reset_view(request):
    if request.method == 'POST':
        form= PasswordResetForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data.get('email')
            user=User.objects.filter(email=email).first()
            if user:
                uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
                token = default_token_generator.make_token(user)
                reset_url = reverse('password_reset_confirm', kwargs={'uidb64': uidb64, 'token': token})
                reset_absolute_url = f'{request.build_absolute_uri(reset_url)}'
                reset_password_email(user.email,reset_absolute_url)
            messages.success(request,'password reset link has been sent')
            return redirect('login')

    else:
        form= PasswordResetForm()
    return render(request, 'account/password_reset.html')



def password_reset_confirm_view(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

        if not default_token_generator.check_token(user, token):
            messages.error(request, 'The reset link is invalid or has expired.')
            return redirect('password_reset')

        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your password has been successfully reset. You can now log in.')
                return redirect('login')
            else:
                for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, error)
        else:
            form = SetPasswordForm(user)

        return render(request, 'account/password_reset_confirm.html', {'form': form})

    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        messages.error(request, 'Error occurred! Please try again.')
        return redirect('password_reset')

   
           
   

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')
