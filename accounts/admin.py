from django.contrib import admin
from django.contrib.auth.forms import AdminPasswordChangeForm

from .models import User, Shop, Address, UserEmail
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import ugettext_lazy as _

class UserAdmin(BaseUserAdmin):
    list_display = ['email', 'is_staff']
    change_password_form = AdminPasswordChangeForm
    ordering = ('email',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'mobile', 'image','password1', 'password2')
        }),
    )
    fieldsets = (
        (_('authentication data'), {
            "fields": (
                'email',
                'password',
            ),
        }),
        (_('Personal info'), {
            "fields": ('first_name', 'image', 'last_name')
        }),
        (_('Permissions'), {
            "fields": ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')
        }),
        (_('Important dates'), {
            "fields": ('last_login',)
        }),
    )


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Shop)
admin.site.register(Address)
admin.site.register(UserEmail)
