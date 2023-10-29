from datetime import date

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


# Create your models here.
class User(AbstractUser):
    birthday = models.DateField(null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    avatar = models.ImageField(upload_to='users/avatars', default='users/avatars/default_avatar.jpg')
    email = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return f"{self.username} {self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse('user_detail', kwargs={'pk': self.user.pk})

    def save(self, *args, **kwargs):
        if self.birthday:
            today = date.today()
            age = today.year - self.birthday.year - (
                    (today.month, today.day) < (self.birthday.month, self.birthday.day))
            self.age = age
        super(User, self).save(*args, **kwargs)