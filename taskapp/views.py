from django.shortcuts import render, redirect
from . import tasks
from . import models
from .forms import ActionTaskForm, IndexForm

def index(request):
    if request.method == 'POST':
        form = IndexForm()
        export = tasks.create_report.delay()
        data_dict = {
        'id_task': export.task_id,
        'status_task': export.get(),
        'widget_list': '-',
        'form': form,
        'total_registers': tasks.count_widgets.delay().get()
        }
        return render(request, 'taskapp/index.html', data_dict)

    form = IndexForm()
    new_register = tasks.create_widget.delay(1)
    list_widget = models.Widget.objects.all()
    data_dict = {
        'id_task': new_register.task_id,
        'status_task': new_register.get(),
        'widget_list': list_widget,
        'form': form,
        'total_registers': len(list_widget)
    }
    return render(request, 'taskapp/index.html', data_dict)

def other_page(request):
    if request.method == 'POST':
        form = ActionTaskForm()
        out_data = tasks.delete_last_widget.delay()
        data_dict = {
            'id_task': out_data.task_id,
            'status_task': out_data.get(),
            'form': form
        }
        return render(request, 'taskapp/other_page.html', data_dict)

    form = ActionTaskForm()
    data_dict = {
        'id_task': '-',
        'status_task': '-',
        'form': form
    }
    return render(request, 'taskapp/other_page.html', data_dict)