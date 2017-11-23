# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime

class LatLon(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()
    def __str__(self):
                return str(self.id)

class SoilMoisture(models.Model):
    moistValue = models.FloatField()
    date = models.DateField(("Date"), default=datetime.date.today)
    latlon = models.ForeignKey(LatLon,on_delete = models.CASCADE)
    def __str__(self):
                return str(self.id)
class WaterFlow(models.Model):
    radius = models.FloatField()
    speed = models.FloatField()
    date = models.DateField(("Date"), default=datetime.date.today)
    time = models.TimeField(("Time"),blank=True)
    latlon = models.ForeignKey(LatLon,on_delete = models.CASCADE)
    def __str__(self):
                return str(self.id)
class WaterLevel(models.Model):
    value = models.FloatField()
    date = models.DateField(("Date"), default=datetime.date.today)
    time = models.TimeField(("Time"),blank=True)
    latlon = models.ForeignKey(LatLon,on_delete = models.CASCADE)
    def __str__(self):
                return str(self.id)
