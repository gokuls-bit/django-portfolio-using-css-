# myapp/models.py

from django.db import models

class Project(models.Model):
    """
    Optional model to store project details in the database.
    For this implementation, projects are hardcoded in the template,
    but this model is provided for future dynamic content management.
    """
    title = models.CharField(max_length=100)
    tech_stack = models.CharField(max_length=200)
    description = models.TextField()
    github_link = models.URLField(blank=True, null=True)
    demo_link = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    """
    Model to store messages submitted through the contact form.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"

