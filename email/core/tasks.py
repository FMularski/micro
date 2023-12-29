from celery import shared_task


@shared_task
def queue_email():
    print("email sent")
