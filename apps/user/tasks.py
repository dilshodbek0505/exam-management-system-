from django.core.mail import send_mail
from django.conf import settings

from celery import shared_task


@shared_task
def send_verification_code(email, code):
    subject = "Parolni tiklash uchun tasdiqlash kodi"

    from_email = settings.DEFAULT_FROM_EMAIL
    user_email_list = [email]

    send_mail(subject, f'Sizning tasdiqlash kodingiz: {code}', from_email, user_email_list)





