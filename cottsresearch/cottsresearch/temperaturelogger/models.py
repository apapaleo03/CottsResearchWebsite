from django.db import models
from django.conf import settings
from model_utils.models import TimeStampedModel
from autoslug import AutoSlugField

class Temperature(TimeStampedModel):
    member = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null = True)
    temp = models.DecimalField(max_digits=5, decimal_places=2)
    
    
    def __str__(self):
        return str(self.member) + '--' + self.created.strftime("%Y-%m-%d %H:%M %p")  + '--'+str(self.temp) + ' F' 