from django.db import models

# Create your models here.

class Profiles(models.Model): # onetoone auth.user
    fname = models.CharField(default='Blank',max_length=50)
    lname = models.CharField(default='Blank', max_length=50)
    id_number = models.IntegerField(default=0) # is it your PK ??
    email = models.CharField(default='Blank',max_length=50)

    def __str__(self):
        return self.fname, self.lname, self.id_number
