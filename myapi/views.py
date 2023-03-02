from django.shortcuts import render
from rest_framework import viewsets
from myapi.models import vehicle
from myapi.serializers import vehicleserailizer
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
class vehicleviewset(viewsets.ModelViewSet):
    queryset=vehicle.objects.all()
    serializer_class=vehicleserailizer
    
    def get_queryset(self):
      #post_id='UK07AH1164'
      plate=self.request.query_params.get('plate')
      #print(plate+'djjjjjj')
      set = vehicle.objects.all()
     
      set=set.filter(plate=plate)
      email=set.values('email')
      email=list(email)
      
      print(email[:3])
      send()
      return(set)
      
      #print (queryset)


def send():
   send_mail(
         'test',
        'Hello',
         'dhruvjindal532@gmail.com',
        ['jindaldhruv614@gmail.com'],
        fail_silently=False,
      )