from django.shortcuts import render,HttpResponseRedirect
from django.contrib import messages
from incidents.forms import SignUpForm,IncidentReportingForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from .models import ReportIncident
from django.contrib.auth import logout

def dashboard(request):
    return render(request, 'html files/dashboard.html')    

#signup form
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request, 'user created successfully')
            form.save()
    else:
        form = SignUpForm()
    return render(request,'html files/registration.html',{'form':form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                messages.success(request, f'{username} logged successfully')
                return HttpResponseRedirect('http://127.0.0.1:8000/profile/')
        else:
            messages.error(request, 'User not found')
    else:
        form = AuthenticationForm()
    form = AuthenticationForm()
    return render(request, 'html files/login.html', {'form': form})


def profile(request):
    username = request.user.username
    return render(request, 'html files/profile.html', {'username': username})


def report_incident(request):
    if request.method == 'POST':
        form = IncidentReportingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Incident reported successfully..')
    else:
        form = IncidentReportingForm()
    form = IncidentReportingForm()
    return render(request, 'html files/report_incident.html', {'form': form})


def saved_incidents(request):
    incidents = ReportIncident.objects.all().values_list()
    return render(request, 'html files/saved_incidents.html', {'incident': incidents})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('http://127.0.0.1:8000/login/')