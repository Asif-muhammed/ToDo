from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Task
from . forms import ToDoform
from django.views.generic.detail import DetailView
# Create your views here.
def index(request):

   task1=Task.objects.all()
   if request.method=='POST':
      name=request.POST.get('task','')
      priority= request.POST.get('priority','')
      time=request.POST.get('date','')
      task=Task(name=name,priority=priority,time=time)
      task.save()

   return render(request,'index.html',{'task':task1})

def delete(request,taskid):

   task=Task.objects.get(id=taskid)
   if request.method=='POST':
      task.delete()
      return redirect('/')

   return render(request,'delete.html')

def update(request,id):

    task=Task.objects.get(id=id)
    f=ToDoform(request.POST or None,instance=task)
    if f.is_valid():
       f.save()
       return redirect('/')

    return render(request,'edit.html',{'f':f,'task':task})

class Detailview(DetailView):
    model = Task
    template_name ='details.html'
    context_object_name ='task'

# def detailview(request,id):
#
#     return render(request,'details.html')