from celery import shared_task

from .models import Factory


@shared_task
def test_cele():
    factory = Factory.objects.all()
    factory.update(debt=1)
