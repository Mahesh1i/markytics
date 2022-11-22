from django.contrib import admin
from .models import ReportIncident

@admin.register(ReportIncident)
class ReportIncidentAdmin(admin.ModelAdmin):
    list_display = ['Location', 'Incident_Department', 'Date_of_Incident', 'Time_of_Incident', 'Incident_Location',
                    'Initial_severity', 'Suspected_Cause', 'Immediate_Action_Taken']