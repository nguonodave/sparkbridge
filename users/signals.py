from django.db.models.signals import post_delete
from . models import Customer

'''
use post delete to delete a user when its instance in company or customer table is deleted
'''

def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()

post_delete.connect(deleteUser, sender=Customer)