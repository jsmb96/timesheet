from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy

# Create your models here.

class Profile(models.Model):
    profile = models.OneToOneField(User,on_delete=models.CASCADE) #user
    # id = models.OneToOneField(default=0,on_delete=models.CASCADE) # is it your PK ??
    # email = models.CharField(default='Blank',max_length=50)
    # location = models.CharField(default=1,max_length=50)
    doctor_title = models.CharField(default='',max_length=50)
    image = models.ImageField(upload_to="profiles/", blank=True, null=True)


#add image
    def __str__(self):
        return self.profile.username

    def get_absolute_url(self): #reverve mapping url
        return reverse_lazy('profile:profile_detail', kwargs={'pkr': self.profile.pk, 'pk': self.pk})
