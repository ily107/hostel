from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser,Request

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username','full_name','phone','parent_phone','gender']

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('full_name','phone','parent_phone','gender')}),
    )

admin.site.register(Request)
admin.site.register(CustomUser, CustomUserAdmin)