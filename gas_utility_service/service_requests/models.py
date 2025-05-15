from django.db import models
from django.contrib.auth.models import User

class ServiceRequest(models.Model):
    REQUEST_TYPES = [
        ('GAS_LEAK', 'Gas Leak'),
        ('NEW_CONN', 'New Connection'),
        ('BILL_ISSUE', 'Billing Issue'),
        ('OTHER', 'Other'),
    ]
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('RESOLVED', 'Resolved'),
        ('CLOSED', 'Closed'),
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=20, choices=REQUEST_TYPES)
    description = models.TextField()
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    submitted_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.customer.username} - {self.request_type}"
