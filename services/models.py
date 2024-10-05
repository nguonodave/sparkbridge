from django.db import models
import uuid
from users.models import Company
from users.models import Customer

class Service(models.Model):
    company = models.ForeignKey(Company, default="", on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    description = models.TextField()
    price_hr = models.DecimalField(decimal_places=2, max_digits=5)
    choices = (
        ('Air Conditioner', 'Air Conditioner'),
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
    date = models.DateTimeField(auto_now=True, null=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name
    
class RequestService(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    time = models.IntegerField(default=1)
    total_cost = models.DecimalField(decimal_places=2, max_digits=5)
    date = models.DateTimeField(auto_now=True, null=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
        verbose_name = 'Requested service'
        verbose_name_plural = 'Requested services'

    def __str__(self):
        return f"{self.service.name} by {self.customer.user.username}"
