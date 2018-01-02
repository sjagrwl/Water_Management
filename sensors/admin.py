# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import WaterTank,WaterTap

admin.site.register(WaterTank)
admin.site.register(WaterTap)

