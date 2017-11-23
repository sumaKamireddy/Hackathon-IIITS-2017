# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from server import models
from django.contrib import admin
admin.site.register(models.LatLon)

admin.site.register(models.SoilMoisture)
admin.site.register(models.WaterFlow)
admin.site.register(models.WaterLevel)

# Register your models here.
