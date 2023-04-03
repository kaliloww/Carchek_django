from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin

from apps.cars.models import Car
from apps.cars.serializers import CarSerializer

# Create your views here.
class CarAPIViewSet(GenericViewSet,
                    ListModelMixin,
                    RetrieveModelMixin,
                    CreateModelMixin,
                    UpdateModelMixin,
                    DestroyModelMixin):
    queryset = Car.objects.all()
    serializer_class = CarSerializer