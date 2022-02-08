from django.db import models

# Create your models here.

class User(models.Model):
    fname = models.CharField(default='Blank',max_length=50)
    lname = models.CharField(default='Blank', max_length=50)
    id_number = models.IntegerField(default=0)
    email = models.CharField(default='Blank',max_length=50)

    def __str__(self):
        return self.fname, self.lname, self.id_number