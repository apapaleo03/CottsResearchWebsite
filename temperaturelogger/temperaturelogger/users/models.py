from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):

    # First Name and Last Name Do Not Cover Name Patterns
    # Around the Globe.
    name = models.CharField(
        _("Name of User"), blank=True, max_length=255
    )
    bio = models.TextField("Bio", blank=True)

    def get_absolute_url(self):
        return reverse(
            "users:detail", kwargs={"username": self.username}
        )

class Temperatures(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse(
            "users:detail", kwargs={"username": User.username}
        )
    class Meta:
        ordering = ('-name','-date',)
