from django.urls import path
from rest_framework import routers

from users.views import CleanerView, CityView, CustomerView, AppointmentCreateView

router = routers.SimpleRouter()
router.register('city', CityView, 'city-name')
router.register('cleaner', CleanerView, 'cleaner-name')
router.register('customer', CustomerView, 'customer-name')



urlpatterns = [
    path(r'appointment/', AppointmentCreateView.as_view())
]
urlpatterns += router.urls