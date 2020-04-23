from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from .models import Task
from .forms import TaskForm
# For home page

def index(request):
	tasks = Task.objects.all()
	form = TaskForm()
	if request.method == "POST":
		form = TaskForm(request.POST)
		print(form)
		if form.is_valid():
			form.save()
			return redirect('home')
	return render(request,'tasks/home.html',{'tasks':tasks,
		'form':form})


def update(request,id):
	task = Task.objects.get(id=id)
	form = TaskForm(instance = task)
	if request.method == "POST":
		form = TaskForm(request.POST, instance = task)
		if form.is_valid():
			form.save()
			return redirect('home')

	return render(request,'tasks/update.html',{'task':task,
		'form':form})

def delete(request,id):
	task = Task.objects.get(id=id)
	if request.method == "POST":
		task.delete()
		return redirect('home')
	return render(request,'tasks/delete.html',{'task':task})
