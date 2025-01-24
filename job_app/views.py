from django.shortcuts import render, redirect, get_object_or_404
from .models import JobApplication
from django.db.models import Q


def index(request):
     return render(request, 'index.html')

def home(request):
    query = request.GET.get('q', '')
    jobs = JobApplication.objects.all().order_by('application_date')
    
    if query:
        jobs = jobs.filter(
            Q(job_title__icontains=query) |
            Q(status__icontains=query) 
        )
    
    return render(request, 'home.html', {'jobs': jobs})

from django.http import JsonResponse

def job_detail(request, pk):
    job = get_object_or_404(JobApplication, pk=pk)
    data = {
        'job_title': job.job_title,
        'company_name': job.company_name,
        'application_date': job.application_date,
        'closing_date': job.closing_date,
        'get_status_display': job.get_status_display(),
        'notes': job.notes,
    }
    return JsonResponse(data)


def job_create(request):
    if request.method == 'POST':
        # Recibir los datos directamente del formulario
        job_title = request.POST.get('job_title')
        company_name = request.POST.get('company_name')
        requirements = request.POST.get('requirements', '')
        contact_name = request.POST.get('contact_name', '')
        contact_phone = request.POST.get('contact_phone', '')
        application_date = request.POST.get('application_date')
        closing_date = request.POST.get('closing_date') or None
        status = request.POST.get('status', 'sent')
        notes = request.POST.get('notes', '')

        # Crear la nueva instancia
        JobApplication.objects.create(
            job_title=job_title,
            company_name=company_name,
            requirements=requirements,
            contact_name=contact_name,
            contact_phone=contact_phone,
            application_date=application_date,
            closing_date=closing_date,
            status=status,
            notes=notes,
        )
        return redirect('home')

    return render(request, 'job_form.html', {'action': 'Add'})

def job_update(request, pk):
    job = get_object_or_404(JobApplication, pk=pk)
    if request.method == 'POST':
        job.job_title = request.POST.get('job_title')
        job.company_name = request.POST.get('company_name')
        job.requirements = request.POST.get('requirements', '')
        job.contact_name = request.POST.get('contact_name', '')
        job.contact_phone = request.POST.get('contact_phone', '')
        job.application_date = request.POST.get('application_date')
        job.closing_date = request.POST.get('closing_date') or None
        job.status = request.POST.get('status', 'sent')
        job.notes = request.POST.get('notes', '')
        job.save()
        return redirect('home')

    return render(request, 'job_form.html', {'job': job, 'action': 'Edit'})

def job_delete(request, pk):
    job = get_object_or_404(JobApplication, pk=pk)
    if request.method == 'POST':
        job.delete()
        return redirect('home')
    return render(request, 'job_confirm_delete.html', {'job': job})
