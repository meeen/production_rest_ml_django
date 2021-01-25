from rest_framework import serializers
from .models import production, machine

class production_serializer(serializers.ModelSerializer):
    class Meta:
        model = production
        fields = ('product','machinetime','machine','tooltime','tolarance')

class machine_serializer(serializers.ModelSerializer):
    class Meta:
        model = machine
        fields = ('name','desc','mtype')


       