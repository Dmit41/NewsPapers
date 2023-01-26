from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string

from .models import News, Articles


def send_notifications(description, pk, name, subs_email):
    html_content = render_to_string(
        'post_created_email.html',
        {
            'text': description,
            'link': f'{settings.SITE_URL}/post/{pk}'
        }
    )

    msg = EmailMultiAlternatives(
        subject=name,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subs_email
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()


@receiver(post_save, sender=News)
def add_new_post(sender, instance, **kwargs):
    subs_email = []
    subs = instance.category.subscribers.all()
    subs_email += [s.email for s in subs]

    send_notifications(instance.description, instance.pk, instance.name, subs_email)


@receiver(post_save, sender=Articles)
def add_new_post(sender, instance, **kwargs):
    subs_email = []
    subs = instance.category.subscribers.all()
    subs_email += [s.email for s in subs]

    send_notifications(instance.description, instance.pk, instance.name, subs_email)

