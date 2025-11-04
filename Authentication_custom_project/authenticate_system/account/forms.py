# account/forms.py
from django import forms  # type: ignore
from .models import User

class RegistrationForm(forms.ModelForm):
    role=(
        ('customer','Customer'),
        ('seller','Seller')
    )

    role=forms.ChoiceField(choices=role,widget=forms.Select())
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Enter password'
        })
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Confirm password'
        })
    )

    class Meta:
        model = User
        fields = ['name', 'email']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter your name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter your email'
            }),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError("Passwords don't match")
            
            if len(password1) < 8:
                raise forms.ValidationError("Password must be at least 8 characters long")
        
        return password2

    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.set_password(self.cleaned_data['password1'])
    #     user.is_active = False
    #     user.is_customer = True  # Set default role
    #     if commit:
    #         user.save()
    #     return user
