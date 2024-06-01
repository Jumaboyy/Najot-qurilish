from rest_framework.routers import DefaultRouter
from .views import HududViewSet, QurilishTashkilotiViewSet, QurilishBinisiViewSet

router = DefaultRouter()
router.register('hududlar', HududViewSet)
router.register('qurilish-tashkilotlari', QurilishTashkilotiViewSet)
router.register('qurilish-binolari', QurilishBinisiViewSet)

urlpatterns = router.urls
