
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Campaign, Recipient, Template, EmailLog
from .serializers import (
    CampaignSerializer, RecipientSerializer, TemplateSerializer, EmailLogSerializer
)
from .utils import send_campaign_email_sync

class TemplateViewSet(viewsets.ModelViewSet):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer

class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    
    @action(detail=True, methods=['post'])
    def run(self, request, pk=None):
        campaign = self.get_object()
    
        if send_campaign_email_sync(campaign.id):
            campaign.status = 'FINALIZADA'
            campaign.save()

            return Response({'status': 'Campaña finalizada', 'message': 'Todos los emails se enviaron correctamente.'})
        else:
            return Response({'status': 'Error', 'message': 'Ocurrió un error al enviar los emails.'}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['get'])
    def reporte(self, request, pk=None):
        campaign = self.get_object()
        #crear el reporte en CSV
        return Response({'status': 'OK', 'message': f'Reporte de la campaña {campaign.name} listo para descargar.'})
    
    
class RecipientViewSet(viewsets.ModelViewSet):
    queryset = Recipient.objects.all()
    serializer_class = RecipientSerializer

class EmailLogViewSet(viewsets.ModelViewSet):
    queryset = EmailLog.objects.all()
    serializer_class = EmailLogSerializer