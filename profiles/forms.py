from django import forms
from profiles.models import Profiles

class UserForm(forms.ModelForm):
    class Meta:
        model = Profiles
        fields = ()