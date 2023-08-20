from django.db.models.signals import post_save
from django.dispatch import receiver
from .tasks import notify_add_response, notify_accept_response
from .models import Response

from django.db.models.signals import m2m_changed

 
 
@receiver(post_save, sender=Response)
def notify(sender, instance, created, **kwargs):
    if created:
        notify_add_response(instance)
    else:
        notify_accept_response(instance)