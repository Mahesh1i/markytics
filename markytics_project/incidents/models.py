from django.db import models

incident_location = (
    ('Corporate Headoffice','CORPORATE HEADOFFICE'),
    ('Operations Department', 'OPERATIONS DEPARTMENT'),
    ('Work station','WORK STATION'),
    ('Marketing Division', 'MARKETING DIVISION')
)
severity = (
    ('Mild', 'MILD'),
    ('Moderate', 'MODERATE'),
    ('Severe', 'SEVERE'),
    ('Fatal', 'FATAL'),
)

class ReportIncident(models.Model):
    Location = models.CharField(max_length=200,choices = incident_location, default = 'OPERATIONS DEPARTMENT')
    Incident_Department = models.TextField()
    Date_of_Incident = models.DateField()
    Time_of_Incident= models.TimeField(auto_now_add=False, auto_now=False)
    Incident_Location = models.TextField()
    Initial_severity = models.CharField(max_length=70, choices=severity, default = 'MILD')
    Suspected_Cause = models.TextField()
    Immediate_Action_Taken = models.TextField()
    Sub_Incident_Type = models.SET_NULL
    Environmental_Incident = models.BooleanField(verbose_name='Environmental Incident', default=False)
    Injury = models.BooleanField(verbose_name='Injury/Illness', default=False)
    Property_Damage = models.BooleanField(verbose_name='Property Damage', default=False)
    Vehicle = models.BooleanField(verbose_name='Vehicle', default=False)
