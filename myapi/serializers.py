from rest_framework import serializers
from myapi.models import vehicle

class vehicleserailizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=vehicle
        fields="__all__"