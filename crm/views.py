from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse

from .models import Task

from .forms import TaskForm

# Homepage / first page of the app

def homepage(request):

    clientList = [
        {
            'id': '1',
            'name': 'Jonh',
            'occupation': 'Egineer'
        },

        {
            'id': '2',
            'name': 'Kate',
            'occupation': 'Lawyer'
        }
    ]

    context = {'clientList': clientList}

    return render(request, 'crm/index.html', context)

# CRUD - Read
def tasks(request):
   
   queryDataAll = Task.objects.all()

   context = {'AllTasks': queryDataAll}
   
   return render(request, 'crm/view-tasks.html', context)


# CRUD - Create
def create_task(request):

    form = TaskForm()

    if request.method == 'POST':

        form = TaskForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('view-tasks')


    context = {'TaskForm': form}

    return render(request, 'crm/create-task.html', context)

# Registration webpage

def register(request):

    return render(request, 'crm/register.html')