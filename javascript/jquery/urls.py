from . import views
from django.urls import path


app_name = 'jquery'

urlpatterns = [

    path('',views.map,name='map'),


]