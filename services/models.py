from django.db import models
import uuid

class Service(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    price_hr = models.DecimalField(decimal_places=2, max_digits=100)
    date = models.DateTimeField(auto_now=True, null=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name
