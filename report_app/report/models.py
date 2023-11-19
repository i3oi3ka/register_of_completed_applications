from django.db import models
from django.urls import reverse

from  subscriber.models import Subscriber

from users.models import User


# Create your models here.
class Locality(models.Model):
    name = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class Report(models.Model):
    REPORT_TYPE = (
        ('мідь', 'Мідь'),
        ('pon', 'Pon'),
    )

    subscriber = models.ForeignKey(Subscriber, null=True, blank=True, on_delete=models.SET_NULL)
    city = models.ForeignKey(Locality, on_delete=models.CASCADE)
    street = models.CharField(max_length=50)
    house = models.CharField(max_length=10)
    apartment = models.CharField(max_length=10)
    report_type = models.CharField(max_length=10, choices=REPORT_TYPE, default='мідь')
    cable_fo = models.IntegerField(null=True, blank=True)
    cable_utp = models.IntegerField(null=True, blank=True)
    router = models.BooleanField(default=False)
    tv = models.BooleanField(default=False)
    connection_date = models.DateField(null=False, blank=True)
    executor = models.ForeignKey(User, related_name='executor', null=True, blank=True, on_delete=models.SET_NULL)
    partner = models.ForeignKey(User, related_name='partner', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.report_type} {self.city} {self.street} {self.house} {self.apartment} {self.cable_fo} {self.cable_utp} {self.router} {self.tv}"

    def get_absolute_url(self):
        return reverse('report_detail', kwargs={'pk': self.pk})
