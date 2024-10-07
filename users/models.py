from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

'''
the __str__ method returns the specified field for easy readability in the Django admin
'''

# extending Django’s built-in AbstractUser, allowing for custom user management
class User(AbstractUser):
    is_company = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=100, unique=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False) # override the default id field

    # specifies that the email field should be used as the username for login authentication
    USERNAME_FIELD = 'email'
    # specifies additional list of the field names that will be prompted when creating a user with createsuperuser command
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    d_o_b = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username

class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    choices = (
        ('Air Conditioner', 'Air Conditioner'),
        ('All in One', 'All in One'),
        ('Carpentry', 'Carpentry'),
        ('Electricity', 'Electricity'),
        ('Gardening', 'Gardening'),
        ('Home Machines', 'Home Machines'),
        ('Housekeeping', 'Housekeeping'),
        ('Interior Design', 'Interior Design'),
        ('Locks', 'Locks'),
        ('Painting', 'Painting'),
        ('Plumbing', 'Plumbing'),
        ('Water Heaters', 'Water Heaters'),
    )
    field = models.CharField(max_length=30, blank=False, null=False, default="", choices=choices)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.user.username
