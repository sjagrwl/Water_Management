# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from LoginPortal.models import UserProfile

class WaterTank(models.Model):
    read_time = models.DateTimeField(auto_now=True)
    WaterLevel = models.FloatField()
    Turbidity = models.FloatField(null=True)
    WaterConsumption = models.FloatField(null=True)

    def __str__(self):
        return 'Tank Reading Time '+str(self.read_time.time())

class WaterTap(models.Model):
    read_time = models.DateTimeField(auto_now=True)
    Proximity = models.FloatField()
    WaterFlow = models.FloatField(null=True)

    def __str__(self):
        return 'Tap Reading Time '+str(self.read_time.time())