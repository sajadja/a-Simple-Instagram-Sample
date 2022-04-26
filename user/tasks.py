from time import sleep

from celery import shared_task
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()


@shared_task(name='send verification code')
def send_verification_code(username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return None
    sleep(10)
    print('email received: ', user.email)
    return 'verification code sent to : {}'.format(user.email)


@shared_task()
def minute_pinger():
    print('time: {}'.format(timezone.now()))


@shared_task()
def minute_three_pinger():
    print('time: {}'.format(timezone.now()))


@shared_task()
def check_unverified_users():
    for user in User.objects.all():
        # if user is not verified send verification code
        send_verification_code(user.username)
