from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField
from users.models import Customer
from .models import City, Cleaner


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class CleanerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cleaner
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class AppointmentSerializer(serializers.Serializer):
    phone_number = PhoneNumberField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    date = serializers.DateField()
    from_time = serializers.TimeField()
    to_time = serializers.TimeField()
    city = serializers.PrimaryKeyRelatedField(queryset=City.objects.filter(is_able=True))

