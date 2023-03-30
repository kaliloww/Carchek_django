from django.urls import path

from apps.cars.views import CarAPIView, CarCreateAPIView

urlpatterns = [
    path('cars/', CarAPIView.as_view(), name = "api_cars"),
    path('cars/create/', CarCreateAPIView.as_view(), name = "api_cars_create")
]