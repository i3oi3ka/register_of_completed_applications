from django.db import models
from django.urls import reverse


# Create your models here.

class Subscriber(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    surname = models.CharField(max_length=120)
    phone = models.CharField(max_length=12, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ["first_name", "last_name", "surname"]

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.surname}"

    def get_absolute_url(self):
        return reverse('subscriber_detail', kwargs={'pk': self.pk})
