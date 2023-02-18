from rest_framework import viewsets
from .serializers import LoggerSerializer #impor the serializer we just created
from .models import Logger
 

class logger_view_set(viewsets.ModelViewSet):
    # define queryset
    queryset = Logger.objects.all()
    serializer_class = LoggerSerializer