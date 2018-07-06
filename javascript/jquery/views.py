from django.shortcuts import render
from django.shortcuts import render, redirect,get_object_or_404
from .models import Maps
from django.urls import reverse
import json
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect


def map(request):
    maps = Maps.objects.all()
    if request.method=='POST':

        # address=request.POST['address']
        # country = request.POST['country']
        # postal_code = request.POST['Postal_code']
        return JsonResponse({'saved':'saved'})
    return render(request,'jquery/googlemaps.html',{'maps':maps})

def mapsubmit(request):

    if request.method == 'POST':
        model=Maps()

        model.address=request.POST['address']
        model.country = request.POST['country']
        model.postal_code = request.POST['postal_code']
        print(model.address,model.country,model.postal_code)
        model.save()


        return JsonResponse({'saved': 'saved'})
    return render(request, 'jquery/googlemaps.html')
