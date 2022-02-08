from django.db import models

# Create your models here.
from django.utils import timezone


class Workday(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_info = models.CharField(default='Blank',max_length=50)
    time_in = models.DateTimeField(blank=True, null=True)
    time_out = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.user_info, self.time_in, self.time_out