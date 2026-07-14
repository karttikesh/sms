from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User

@admin.register(User)
class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User

    list_display = ('name','username','email','mobile','is_active','joined_date','last_updated')
    search_fields = ('email','username','mobile')
    list_filter = ('is_active','is_staff','joined_date')
    ordering = ('joined_date',)

    fieldsets = (
        (None,               {'fields': ('username', 'password')}),
        ('Personal info',    {'fields': ('name','mobile','email')}),
        ('Permissions',      {'fields': ('is_active','is_staff',)}),
        ('Groups & perms',   {'fields': ('groups','user_permissions')}),
        ('Important dates',  {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','mobile','email','name','password1','password2','is_active',
                       'is_staff',)},
        ),
    )
    filter_horizontal = ('groups','user_permissions')