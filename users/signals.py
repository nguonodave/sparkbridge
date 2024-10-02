from django.db.models.signals import post_delete
from . models import Customer

def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()

post_delete.connect(deleteUser, sender=Customer)