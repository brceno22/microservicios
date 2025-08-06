from rest_framework import serializers
from .models import Template, Campaign, Recipient, EmailLog

class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
        
class CampaignSerializer(serializers.ModelSerializer):
    template = TemplateSerializer()
    
    class Meta:
        model = Campaign
        fields = [
            'id',
            'name',
            'template',
            'start_date',
            'end_date',
            'status',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'status', 'created_at', 'updated_at']

class RecipientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipient
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
        
class EmailLogSerializer(serializers.ModelSerializer):
    campaign = CampaignSerializer(read_only=True)
    recipient = RecipientSerializer(read_only=True)
    class Meta:
        model = EmailLog
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at', 'sent_at']
        