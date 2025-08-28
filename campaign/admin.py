from django.contrib import admin

from .models import Campaign, Recipient, Template, EmailLog

admin.site.register(Campaign)
admin.site.register(Recipient)
admin.site.register(Template)
admin.site.register(EmailLog)
