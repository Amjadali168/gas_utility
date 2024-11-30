from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

class ServiceRequest(models.Model):
    SERVICE_CHOICES = [
        ('installation', 'Installation'),
        ('repair', 'Repair'),
        ('billing', 'Billing Issue'),
        ('other', 'Other'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    details = models.TextField()
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(blank=True, null=True)

class SupportRepresentative(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)