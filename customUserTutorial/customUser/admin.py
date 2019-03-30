from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active', )
    list_filter = ('email', 'is_staff', 'is_active', )
    fieldsets = (
        (None, {'fields': ('email', 'password', 'is_seller', 'is_buyer', 'is_advertiser', 'account_credits', )}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_seller', 'is_buyer', 'is_advertiser', 'account_credits', 'is_staff', 'is_active')}),
    )
    search_fields = ('email', )
    ordering = ('email', )


admin.site.register(CustomUser, CustomUserAdmin)
