from rest_framework.routers import DefaultRouter, SimpleRouter

from entity.views import EntityViewSet

router = SimpleRouter()

app_name = "api_v1"

router.register('entity', EntityViewSet, basename='entity')

urlpatterns = router.urls
