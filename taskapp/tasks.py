# Create your tasks here

from celery import shared_task
from taskapp.models import Widget
from time import sleep
from datetime import datetime


@shared_task
def create_widget(n_register):
    for i in range(n_register):
        tagDatetime = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        w = Widget()
        w.name = f'CW_{tagDatetime}'
        w.save()
        print(f'CW_{tagDatetime} | Widget created')
    return f'All Widgets created'


@shared_task
def count_widgets():
    return Widget.objects.count()


@shared_task
def rename_widget(widget_id, name):
    w = Widget.objects.get(id=widget_id)
    w.name = name
    w.save()

@shared_task
def delete_last_widget():
    try:
        w = Widget.objects.all().last().delete()
        return f'Last deleted with sucess!'
    except:
        return f'Falid in erase last registers !'

@shared_task
def delete_all_widget():
    try:
        w = Widget.objects.all().delete()
        return f'All registers erased with sucess!'
    except:
        return f'Falid in erase all registers !'

@shared_task
def create_report():
    data_list = Widget.objects.all()
    with open('report.txt', 'w') as report:
        for data in data_list:
            report.write(f'{data.name}\n')
            sleep(1)
    return 'Sucess Report Widget Data'