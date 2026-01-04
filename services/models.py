from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Service(models.Model):
    CATEGORY_CHOICES = [
        ('TECH', 'Technology & Coding'),
        ('DESIGN', 'Graphics & Design'),
        ('ACADEMIC', 'Tutoring & Academic'),
        ('ERRANDS', 'Errands & Laundry'),
        ('KRA', 'KRA Returns Filing Services'),
        ('OTHER', 'Other Services'),
    ]

    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='services')
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='ERRANDS')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title