from celery import Celery, group

from django.contrib.auth.models import User
from django.core.mail import send_mail

from django_human_project import settings

app = Celery()


@app.task
def send_emails():
    emails = User.objects.exclude(email='').values_list('email', flat=True).distinct()
    g = group(send_email.s(email) for email in emails)
    g.apply_async()


@app.task
def send_email(email):
    subject = "Daily message"
    message = "Have a nice day!"
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])

