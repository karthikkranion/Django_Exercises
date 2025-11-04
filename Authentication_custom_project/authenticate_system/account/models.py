# models.py
from django.db import models  # type: ignore
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin # type: ignore


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have a valid email")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)  # ADD THIS!
        extra_fields.setdefault('is_customer', False)
        extra_fields.setdefault('is_seller', False)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):  # Add PermissionsMixin
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=250)
    city = models.CharField(max_length=100, default="",blank=False,null=False)  # Fixed
    is_active = models.BooleanField(default=False) 
    is_staff = models.BooleanField(default=False)  
    is_superuser = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)  
    is_customer = models.BooleanField(default=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']  # Add this - fields required when creating superuser

    objects = UserManager()

    def __str__(self):
        return self.email
    
    # Remove has_perm and has_module_perms - PermissionsMixin handles these
    def has_perm(self, perm, obj=None):
        return self.is_superuser or super().has_perm(perm, obj)

    def has_module_perms(self, app_label):
        return self.is_superuser or super().has_module_perms(app_label)
    