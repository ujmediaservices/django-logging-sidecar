from dataclasses import fields
from rest_framework import serializers
from .models import Logger
 
# create a serializer
class LoggerSerializer(serializers.Serializer):
    # initialize model and fields you want to serialize
    class Meta:
        model = Logger
        fields = ('message', 'date_time')