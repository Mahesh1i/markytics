from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User 
from .models import ReportIncident
from django import forms

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'email': 'Email'}
        
    
class IncidentReportingForm(forms.ModelForm):
    class Meta:
        model = ReportIncident
        fields = '__all__'
        widgets = {
            'Date_of_Incident': forms.DateInput(format=('%d-%m-%Y'), 
                                             attrs={'class':'myDateClass', 
                                            'placeholder':'Select a date'})
        }

        

        