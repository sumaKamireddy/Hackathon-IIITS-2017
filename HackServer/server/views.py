# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from server import models
import csv
#class SoilMoistureList(APIView):
def SoilMoistureList(request):
    i=0
    with open('/home/vagdevi/Desktop/testp/data/new.csv', 'rb') as csvfile:
         spamreader = csv.reader(csvfile)
         for row in spamreader:
             i=0
    k=row
    objects = models.SoilMoisture.objects.all()
    latlonob=models.LatLon.objects.all()
    l=[]
    val=[]
    li=[]
    models.SoilMoisture.objects.select_for_update().filter(id=1).update(moistValue = float(k[0]))
    for i in range(0,8):
        #id=objects[i].latlon

        val.append(objects[i].moistValue)
        for j in range(0,8):
            #print latlonob[j].id,
            #print type(objects[i].latlon.id)
            if latlonob[j].id ==objects[i].latlon.id:

                l.append(latlonob[j].lat)
                l.append(latlonob[j].lon)
                break

    # obj=SoilMoisture.objects.get(id=1)
    # obj.moistValue=float(k[0])
    # obj.save()
    # objects = models.SoilMoisture.objects.all()
    # #serializer = serializers.SoilMoistureSerializer(objects, many=True)
    context={'l':l,'val':val}
    return render(request,'server/moisture.html',context)
#class WaterFlowList(APIView):
def WaterFlowList(request):

    i=0
    with open('/home/vagdevi/Desktop/testp/data/new.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile )
        for row in spamreader:
            i=0
    k=row

    objects = models.WaterFlow.objects.all()
    #models.WaterFlow.objects.select_for_update().filter(id=3).update(speed = float(k[2])+objects[2].speed)
    #serializer = serializers.SoilMoistureSerializer(objects, many=True)
    l=[]
    p=objects[0].speed
    for i in range(0,8):

        if objects[i].id==1:
            models.WaterFlow.objects.select_for_update().filter(id=1).update(speed = (float(k[2])/2)+objects[i].speed)
        else:
            models.WaterFlow.objects.select_for_update().filter(id=i+1).update(speed = 1*objects[i].speed)
        l.append(objects[i].speed)
    return render(request,'server/areaWater.html',{'l':l,'obj':p,'k':float(k[2])})



        #
        # objects = models.WaterFlow.objects.all()
        # #serializer = serializers.WaterFlowSerializer(objects, many=True)
        # context={}
        # return render(request,'#',context)
#class WaterLevelList(APIView):
def WaterLevelList(request):
    i=0
    with open('/home/vagdevi/Desktop/testp/data/new.csv', 'rb') as csvfile:
         spamreader = csv.reader(csvfile)
         for row in spamreader:
             i=0
    k=row
    objects = models.WaterFlow.objects.all()
    latlonob=models.LatLon.objects.all()
    l=[]
    val=[]
    li=[]
    models.WaterFlow.objects.select_for_update().filter(id=1).update(speed = float(k[2]))
    for i in range(0,8):
        #id=objects[i].latlon

        val.append(objects[i].speed)
        max_i=max(val)
        ind1=val.index(max_i)
        min_i=min(val)
        ind2=val.index(min_i)

        for j in range(0,8):
            #print latlonob[j].id,
            #print type(objects[i].latlon.id)
            if latlonob[j].id ==objects[i].latlon.id:

                l.append(latlonob[j].lat)
                l.append(latlonob[j].lon)
                break

    # obj=SoilMoisture.objects.get(id=1)
    # obj.moistValue=float(k[0])
    # obj.save()
    # objects = models.SoilMoisture.objects.all()
    # #serializer = serializers.SoilMoistureSerializer(objects, many=True)
    context={'l':l,'val':val,'ind1':ind1,'ind2':ind2}
    return render(request,'server/distribution.html',context)
def LatLonList(request):
    objects = models.LatLon.objects.all()
    #serializer = serializers.LatLonSerializer(objects, many=True)
    #return Response(serializer.data)
    context={}
    return render(request,'#',context)
