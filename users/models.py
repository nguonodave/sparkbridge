from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(AbstractUser):
    is_company = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=100, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    d_o_b = models.DateField(null=True, blank=True)

class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    choices = (
        ('Air Conditioner', 'Air Conditioner'),
        ('All in One', 'All in One'),
        ('Carpentry', 'Carpentry'),
        ('Electricity', 'Electricity'),
        ('Gardening', 'Gardening'),
        ('Home Machines', 'Home Machines'),
        ('House Keeping', 'House Keeping'),
        ('Interior Design', 'Interior Design'),
        ('Locks', 'Locks'),
        ('Painting', 'Painting'),
        ('Plumbing', 'Plumbing'),
        ('Water Heaters', 'Water Heaters'),
    )
    field = models.CharField(max_length=30, blank=False, null=False, default="", choices=choices)

    def __str__(self):
        return str(self.user.id) + ' - ' + self.user.username

@receiver(post_save, sender=User)
def CreateCustomer(sender, instance, created, **kwargs):
    if created:
        user = instance
        Customer.objects.create(
            user=user
        )
