from django.shortcuts import render, redirect, get_object_or_404
from .models import JobApplication
from .forms import JobApplicationForm


def index(request):
     return render(request, 'index.html')

def home(request):
    jobs = JobApplication.objects.all()
    return render(request, 'home.html', {'jobs': jobs})

def job_create(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = JobApplicationForm()
    return render(request, 'job_form.html', {'form': form, 'action': 'Add'})

def job_update(request, pk):
    job = get_object_or_404(JobApplication, pk=pk)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = JobApplicationForm(instance=job)
    return render(request, 'job_form.html', {'form': form, 'action': 'Edit'})

def job_delete(request, pk):
    job = get_object_or_404(JobApplication, pk=pk)
    if request.method == 'POST':
        job.delete()
        return redirect('home')
    return render(request, 'job_confirm_delete.html', {'job': job})
