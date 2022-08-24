from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserLog(models.Model):
    phone = models.CharField(blank=False, max_length=11)
    otp = models.CharField(max_length=6, null=True, blank=True)
    isVarified = models.BooleanField(blank=False, default=False)

    def __str__(self):
        return str(self.phone)
