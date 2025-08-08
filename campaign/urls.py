from rest_framework.routers import DefaultRouter
from .views import TemplateViewSet, CampaignViewSet, RecipientViewSet, EmailLogViewSet

router = DefaultRouter()
router.register(r'templates', TemplateViewSet)
router.register(r'campaigns', CampaignViewSet)
router.register(r'recipients', RecipientViewSet)
router.register(r'emaillogs', EmailLogViewSet)

urlpatterns = router.urls