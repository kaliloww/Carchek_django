from rest_framework.generics import ListAPIView, CreateAPIView
from django_filters.rest_framework import DjangoFilterBackend

from apps.cars.models import Car
from apps.cars.serializers import CarSerializer

# Create your views here.
class CarAPIView(ListAPIView):
    queryset = Car.objects.all() #SELECT * FROM cars_car;
    serializer_class = CarSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['license_plate', ]

class CarCreateAPIView(CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer