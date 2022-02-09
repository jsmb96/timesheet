from django import forms
from workday.models import Workday

class WorkdayForm(forms.ModelForm):
    class Meta:
        model = Workday
        fields = '__all__'
        # exclude = ('user', 'date')