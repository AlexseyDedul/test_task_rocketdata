import random
from django.utils import timezone

from celery import shared_task
from django_celery_beat.models import PeriodicTask, IntervalSchedule, CrontabSchedule

from .models import Factory, Dilercenter, Distributor, IndividualEntrepreneur, RetailChain

schedule_every_3_hours, created = IntervalSchedule.objects.get_or_create(
    every=3,
    period=IntervalSchedule.HOURS,
)
schedule_one_day, _ = CrontabSchedule.objects.get_or_create(
    minute='30',
    hour='6',
)

try:
    PeriodicTask.objects.create(
        interval=schedule_every_3_hours,
        name='schedule_every_3_hours',
        task='random_increment_debt_for_providers',
    )
    PeriodicTask.objects.create(
        crontab=schedule_one_day,
        name='random_decrement_debt_for_providers',
        task='random_decrement_debt_for_providers',
    )
except:
    pass


@shared_task(name='random_increment_debt_for_providers')
def random_increment_debt_for_providers():
    factories = Factory.objects.all()
    if factories:
        for factory in factories:
            factory.debt = factory.debt - random.randrange(5, 500)
            factory.save()
    dilercenter = Dilercenter.objects.all()
    if dilercenter:
        for dc in dilercenter:
            dc.debt = dc.debt - random.randrange(5, 500)
            dc.save()

    distributors = Distributor.objects.all()
    if distributors:
        for distributor in distributors:
            distributor.debt = distributor.debt - random.randrange(5, 500)
            distributor.save()

    retail_chain = RetailChain.objects.all()
    if retail_chain:
        for rc in retail_chain:
            rc.debt = rc.debt - random.randrange(5, 500)
            rc.save()

    individual_entrepreneur = IndividualEntrepreneur.objects.all()
    if individual_entrepreneur:
        for ie in individual_entrepreneur:
            ie.debt = ie.debt - random.randrange(5, 500)
            ie.save()


@shared_task(name='random_decrement_debt_for_providers')
def random_decrement_debt_for_providers():
    factories = Factory.objects.all()
    if factories:
        for factory in factories:
            factory.debt = factory.debt + random.randrange(100, 10000)
            factory.save()
    dilercenter = Dilercenter.objects.all()
    if dilercenter:
        for dc in dilercenter:
            dc.debt = dc.debt + random.randrange(100, 10000)
            dc.save()

    distributors = Distributor.objects.all()
    if distributors:
        for distributor in distributors:
            distributor.debt = distributor.debt + random.randrange(100, 10000)
            distributor.save()

    retail_chain = RetailChain.objects.all()
    if retail_chain:
        for rc in retail_chain:
            rc.debt = rc.debt + random.randrange(100, 10000)
            rc.save()

    individual_entrepreneur = IndividualEntrepreneur.objects.all()
    if individual_entrepreneur:
        for ie in individual_entrepreneur:
            ie.debt = ie.debt + random.randrange(100, 10000)
            ie.save()


# @shared_task(serializer='json')
# def update_debt(obj_id):
#     print(obj_id)
    # obj = Factory.objects.get(id=obj_id.id)
    # obj.debt = 2
    # obj.save()
