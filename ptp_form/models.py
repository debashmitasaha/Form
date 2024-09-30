from django.db import models

# Create your models here.


class PreTaskForm(models.Model):
    project = models.CharField(max_length=255)
    contractor = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    task = models.TextField()
    notes = models.TextField(blank=True)

    # Add more fields based on the PDF form
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.project} - {self.task}"
