from django.http import HttpResponse,HttpResponseRedirect
from .models import WaterTank,WaterTap,UserProfile
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.views import generic
from LoginPortal.forms import UserForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    template = 'sensors/index.html'
    return render(request,template,{'username':request.user})

@method_decorator(login_required,name='dispatch')
class WaterTankView(generic.ListView):
    template_name = 'sensors/waterTank.html'
    context_object_name='waterTanksensors'

    def get_queryset(self):
        return WaterTank.objects.all()

@method_decorator(login_required,name='dispatch')
class WaterTapView(generic.ListView):
    template_name = 'sensors/waterTap.html'
    context_object_name='waterTapsensors'

    def get_queryset(self):
        return WaterTap.objects.all()

@csrf_exempt
def add_reading(request):
    if request.POST.get('tank'):
        new_reading = WaterTank()
        new_reading.WaterLevel = 15 - float(request.POST.get('tank').split(' ')[0])
        new_reading.Turbidity = float(request.POST.get('tank').split(' ')[1])
        new_reading.WaterConsumption = float(request.POST.get('tank').split(' ')[2].strip('\n'))
        new_reading.save()

        return HttpResponse(status=200)

    if request.POST.get('tap'):
        new_reading= WaterTap()
        new_reading.Proximity = float(request.POST.get('tap').split(' ')[0])
        new_reading.WaterFlow = float(request.POST.get('tap').split(' ')[1].strip('\n'))
        new_reading.save()

        return HttpResponse(status=200)
    return  HttpResponse(status=400)