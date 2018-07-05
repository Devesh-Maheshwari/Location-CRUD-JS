from django.shortcuts import render
from django.shortcuts import render, redirect,get_object_or_404
from .models import Maps
from django.urls import reverse
import json
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect


def map(request):
    return render(request,'jquery/googlemaps.html')
