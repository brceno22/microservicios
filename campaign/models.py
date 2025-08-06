from django.db import models
from .base_models import BaseModel

class Template(BaseModel):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.name

class Campaign(BaseModel):
    STATUS_CHOICES = [
        ('PROCESANDO', 'Procesando'),
        ('FINALIZADA', 'Finalizada'),
        ('PAUSADA', 'Pausada'),
    ]
    name = models.CharField(max_length=255)
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='PROCESANDO')
    #is_active = models.BooleanField(default=True)
    #is_finish = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
class Recipient(BaseModel):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='recipients')
    email = models.EmailField(max_length=255)
    name = models.CharField(max_length=255)
    data_json = models.JSONField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.email} - {self.campaign.name}"
    
class EmailLog(BaseModel):  
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    recipient = models.ForeignKey(Recipient, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    sent_at = models.DateTimeField(auto_now_add=True)
    message_content = models.TextField(blank=True, null=True)
    error_message = models.TextField(blank=True, null=True)
    
    
    
    
    
    
    
