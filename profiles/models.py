from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    profile = models.ForeignKey(User,primary_key=True, default=1, on_delete=models.CASCADE)
    # fname = models.CharField(default='Blank',max_length=50)
    # lname = models.CharField(default='Blank', max_length=50)
    id = models.IntegerField(default=0) # is it your PK ??
    # email = models.CharField(default='Blank',max_length=50)
    location = models.CharField(default='Blank',max_length=50)

    def __str__(self):
        return self.fname, self.lname, self.id_number
