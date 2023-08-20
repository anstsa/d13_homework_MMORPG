from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from .models import Advertisement
from django.contrib.auth.models import User
import datetime


def notify_add_response(instance):
    email_author = Advertisement.objects.get(id=instance.advertisement_id).author.email
    advertisement = instance.advertisement
    html = render_to_string(
        template_name='mail/new_response.html',
        context={
            'response': instance,
            'advertisement': advertisement,
        },
    )

    msg = EmailMultiAlternatives(
        subject='Новый отклик',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[email_author, ]
    )
    msg.attach_alternative(html, 'text/html')
    msg.send()


def notify_accept_response(instance):
    email_author = instance.author.email
    advertisement = instance.advertisement
    html = render_to_string(
        template_name='mail/accept_response.html',
        context={
            'response': instance,
            'advertisement': advertisement,
        },
    )

    msg = EmailMultiAlternatives(
        subject='Ваш отклик принят',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[email_author, ]
    )
    msg.attach_alternative(html, 'text/html')
    msg.send()
    

def notify_weekly():
    email_list = list(User.objects.values_list("email", flat=True))
    end_date = datetime.datetime.now()
    start_date = end_date - datetime.timedelta(days=7)
    advertisements = Advertisement.objects.filter(datatime__range=(start_date, end_date))
    print ('end_date',end_date,'start_date', start_date, advertisements)
    for email in email_list:
        html = render_to_string(
            template_name='mail/weekly_mailing.html',
            context={
                'advertisements': advertisements,
            },
        )

        
        msg = EmailMultiAlternatives(
            subject='Новые обявления',
            body='',
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[email, ],
        )
        msg.attach_alternative(html, 'text/html')
        msg.send()