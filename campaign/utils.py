from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from .models import Campaign, Recipient, EmailLog
from django.utils import timezone

def send_campaign_email_sync(campaign_id):
    try:
        campaign = Campaign.objects.get(id=campaign_id)
        template = campaign.template
        recipients = campaign.recipients.all()

        for recipient in recipients:
            # Aquí personalizamos el contenido usando las variables que ya existen
            email_body = template.content.replace('{recipient_name}', recipient.name)
            print(f'{email_body}')

            # Y usamos el subject de la plantilla
            send_mail(
                subject=template.subject,
                message=email_body,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[recipient.email],
                fail_silently=False,
            )
            print('enviado')
            # Creamos un log del email para registrar el envío
            EmailLog.objects.create(
                campaign=campaign,
                recipient=recipient,
                status='ENVIADO',
                sent_at=timezone.now()
            )

        return True

    except Exception as e:
        print(f"Error al enviar la campaña: {e}")
        return False