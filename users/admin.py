from django.contrib import admin
from . models import User, Customer, Company
from django.contrib.auth.admin import UserAdmin

# extends django’s built-in UserAdmin, allowing fcustomization of how users are displayed in the admin interface
@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ("username", "email", 'is_company', 'is_customer', "id")

    # adds filtering options in the admin interface sidebar, allowing admins to filter users by their status
    list_filter = ('is_company', 'is_customer', 'is_staff', 'is_superuser', 'is_active')

    # organizes how user fields are presented on the user detail/edit form
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('User type', {'fields': ('is_company', 'is_customer')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # specifies the fields shown when adding a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'is_company', 'is_customer'),
        }),
    )

# how objects are displayed in the admin dashboard
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("user", "field")


# how objects are displayed in the admin dashboard
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("user", "d_o_b")
