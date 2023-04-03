from rest_framework import routers

from apps.cars.views import CarAPIViewSet

router = routers.DefaultRouter()
router.register('', CarAPIViewSet, "api_cars")

urlpatterns = router.urls