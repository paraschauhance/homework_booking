from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=155, unique=True)
    is_able = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Cleaner(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Customer(models.Model):
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    phone_number = PhoneNumberField(unique=True)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Appointment(models.Model):
    customer = models.ForeignKey(Customer,blank=True, null=True, on_delete=models.SET_NULL)
    cleaner = models.ForeignKey(Cleaner, blank=True, null=True, on_delete=models.SET_NULL, related_name='booked_appointment')
    date = models.DateField()
    from_time = models.TimeField()
    to_time = models.TimeField()

    def __str__(self):
        return self.customer