from django.contrib import admin # type: ignore
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin # type: ignore
from .models import User

class UserModelAdmin(BaseUserAdmin):
    model = User

    # Fields to display in the list view
    list_display = ('email', 'name', 'is_staff', 'is_superuser', 'is_seller', 'is_customer','is_active')
    list_filter = ('is_superuser', 'is_staff', 'is_seller', 'is_customer')
    search_fields = ('email', 'name')
    ordering = ('email',)  # NOTE: comma makes it a tuple
    

    fieldsets = (
            ("User credentials", {'fields': ('email', 'password')}),
            ('Personal Info', {'fields': ('name', 'city')}),
            ('Permissions', {
                'fields': (
                    'is_active', 'is_staff', 'is_superuser', 'is_seller', 'is_customer',
                    'groups', 'user_permissions'  # <-- ADD THESE!
                )
            }),
        )
    add_fieldsets = (
            (None, {
                'classes': ('wide',),
                'fields': (
                    'email', 'name', 'city',
                    'password1', 'password2',
                    'is_active', 'is_staff', 'is_superuser', 'is_seller', 'is_customer',
                    'groups', 'user_permissions'  # <-- ADD THESE!
                ),
            }),
        )
    filter_horizontal = ('groups', 'user_permissions')  # <-- Best for UI


# Register your custom user model
admin.site.register(User, UserModelAdmin)
