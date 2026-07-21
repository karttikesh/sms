from django import forms
from .models import School

class SchoolForm(forms.ModelForm):
    MODE_CHOICES = (
        ('online', 'Online'),
        ('offline', 'Offline'),
        ('distance', 'Distance Education'),
        ('on_demand', 'On Demand')
    )
    mobile = forms.CharField()
    email = forms.EmailField()
    mode = forms.CharField(widget=forms.Select(choices=MODE_CHOICES))
    affiliation = forms.CharField()
    class Meta():
        model = School
        fields = ['name', 'address', 'state', 'city', 'user', 'mobile', 'email', 'mode', 'affiliation']
