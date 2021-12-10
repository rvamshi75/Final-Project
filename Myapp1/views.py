from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Tasklist
from .forms import TaskForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.



def index(request):
    dict1={'index_text':'Home Page'}
    return render(request,'index.html',dict1)


@login_required

def input(request):
    if request.method=="POST":
        fm=TaskForm(request.POST or None)
        if fm.is_valid():
            fm.save()
        messages.success(request,("New Task Added"))
        return redirect('input')
    else:
        all_tasks = Tasklist.objects.all()
        paginator = Paginator(all_tasks,5)
        page=request.GET.get('pg')
        all_tasks = paginator.get_page(page)
        return render(request,'base.html',{'all_tasks':all_tasks})



def contact(request):
    dict1={'contact':'Contact Us'}
    return render(request,'contact.html',dict1)



def about(request):
    dict1={'aboutus':'About Us'}
    return render(request,'about.html',dict1)



def delete_task(request,task_id):
    task = Tasklist.objects.get(pk=task_id)
    task.delete()
    return redirect('input')



def edit_task(request,task_id):
    if request.method=="POST":
        task_obj = Tasklist.objects.get(pk=task_id)
        fm=TaskForm(request.POST, instance=task_obj)
        if fm.is_valid():
            fm.save()

        messages.success(request,("Task Updated..!!"))
        return redirect('input')
    else:
        task_obj = Tasklist.objects.get(pk=task_id)
        return render(request,'edit.html',{'task_obj':task_obj})





def complete_task(request,task_id):
    task = Tasklist.objects.get(pk=task_id)
    task.done=True
    task.save()
    return redirect('input')




def incomplete_task(request,task_id):
    task = Tasklist.objects.get(pk=task_id)
    task.done=False
    task.save()
    return redirect('input')
