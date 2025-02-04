from django.shortcuts import render, redirect, get_object_or_404
from .models import JobApplication
from django.http import JsonResponse, HttpResponse
from django.db.models import Q
import csv


def index(request):
     return render(request, 'index.html')

def home(request):
    query = request.GET.get('q', '')
    jobs = JobApplication.objects.all().order_by('application_date')
    
    if query:
        jobs = jobs.filter(
            Q(company_name__icontains=query) |
            Q(job_title__icontains=query) |
            Q(status__icontains=query) 
        )
    
    return render(request, 'home.html', {'jobs': jobs})


def job_detail(request, pk):
    job = get_object_or_404(JobApplication, pk=pk)
    data = {
        'job_title': job.job_title,
        'requirements': job.requirements,
        'contact_name': job.contact_name,
        'contact_phone': job.contact_phone,
        'company_name': job.company_name,
        'application_date': job.application_date,
        'closing_date': job.closing_date,
        'status': job.status,
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


def bulk_update_status(request):
    if request.method == 'POST':
        job_ids = request.POST.getlist('job_ids')  # Lista de IDs seleccionados
        new_status = request.POST.get('status')    # Nuevo estado

        if job_ids and new_status:
            # Convertir a int si deseas mayor seguridad
            job_ids_int = [int(x) for x in job_ids]
            JobApplication.objects.filter(pk__in=job_ids_int).update(status=new_status)

        return redirect('home')

    return redirect('home')

def generate_report_csv(request):
    status = request.GET.get('status', 'sent')
    jobs = JobApplication.objects.filter(status=status).order_by('application_date')

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="job_report_{status}.csv"'

    # Cambiamos el delimitador a ";" en lugar de ","
    writer = csv.writer(response, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    # Encabezados de la tabla
    writer.writerow(["ID", "Job Title", "Company", "Application Date", "Closing Date", "Status", "Notes"])

    # Datos de la tabla
    for job in jobs:
        writer.writerow([
            job.id,
            job.job_title,
            job.company_name,
            job.application_date.strftime('%Y-%m-%d') if job.application_date else "N/A",
            job.closing_date.strftime('%Y-%m-%d') if job.closing_date else "N/A",
            job.get_status_display(),
            job.notes if job.notes else "N/A",
        ])

    return response