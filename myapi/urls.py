from django.contrib import admin
from django.urls import path,include
from myapi.views import vehicleviewset
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'vehicles',vehicleviewset)
urlpatterns = [

    path('',include(router.urls))
    
]
