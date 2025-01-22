from django.db import models

class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('sent', 'Enviado'),
        ('in_progress', 'En proceso'),
        ('completed', 'Finalizado'),
    ]

    job_title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    requirements = models.TextField(blank=True, null=True)
    contact_name = models.CharField(max_length=255, blank=True, null=True)
    contact_phone = models.CharField(max_length=15, blank=True, null=True)
    application_date = models.DateField()
    closing_date = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='sent'
    )  # Nuevo campo de estado

    def __str__(self):
        return f"{self.job_title} at {self.company_name} ({self.get_status_display()})"
