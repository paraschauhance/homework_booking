from rest_framework import viewsets, status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from users.serializers import CitySerializer, CleanerSerializer, CustomerSerializer, AppointmentSerializer
from .models import City, Cleaner, Customer, Appointment


class CityView(viewsets.ModelViewSet):
    queryset = City.objects.filter(is_able=True)
    serializer_class = CitySerializer


class CleanerView(viewsets.ModelViewSet):
    queryset = Cleaner.objects.filter()
    serializer_class = CleanerSerializer


class CustomerView(viewsets.ModelViewSet):
    queryset = Customer.objects.filter()
    serializer_class = CustomerSerializer

class AppointmentCreateView(CreateAPIView):
    serializer_class = AppointmentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            import pdb;pdb.set_trace()
            phone_number = serializer.validated_data.get('phone_number')
            first_name = serializer.validated_data.get('first_name')
            last_name = serializer.validated_data.get('last_name')
            city = serializer.validated_data.get('city')
            date = serializer.validated_data.get('date')
            from_time = serializer.validated_data.get('from_time')
            to_time = serializer.validated_data.get('to_time')

            cust = Customer.objects.filter(phone_number=phone_number).first()
            if not cust:
                cust = Customer.objects.create(phone_number=phone_number, first_name = first_name, last_name = last_name, city_id = city.id)
                cust.save()
            city_cleaner = Cleaner.objects.filter(city_id = city).values_list('id')
            available_cleaners = Appointment.objects.filter(cleaner__city_id = city.id,date=date, from_time__range=[from_time, to_time], to_time__range=[from_time, to_time]).values_list('cleaner')
            remainint_cleaner = set(city_cleaner) - set(available_cleaners)
            if remainint_cleaner:
                cleaner = remainint_cleaner.pop()[0]
                appointment = Appointment.objects.create(customer=cust, cleaner_id=cleaner,
                                           date=date, from_time=from_time, to_time=to_time)
                msg = {"message" : "you appoint has been accepted by {}".format(appointment.cleaner)}
            else:
                msg = {"message": "Sorry! try another time to get appointment"}

        return Response(msg, status=status.HTTP_201_CREATED)
