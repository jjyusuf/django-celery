from celery import shared_task
from celery.decorators import task
from celery.utils.log import get_task_logger
from .email import send_review_email

logger = get_task_logger(__name__)

@shared_task
def add(x, y):
    return x + y

@shared_task
def send_email(email, subject, message):
    return 'Email sent to webmaster from {} with body {} and subject {}'.format(email, subject, message)


@task(name="send_review_email_task")
def send_review_email_task(name, email, review):
    logger.info("Sent Comment Email")
    return send_review_email(name, email, review)



