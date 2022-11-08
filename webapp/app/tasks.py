from celery import app

from .models import Factory


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(30.0, test.s(), name='add every 10')


@app.task
def test():
    factory = Factory.objects.all()
    factory.update(debt=1)


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'tasks.test',
        'schedule': 30.0,
        'args': ()
    },
}
app.conf.timezone = 'UTC'
