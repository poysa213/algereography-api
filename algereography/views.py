from django.shortcuts import render

from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Wilaya, Daira
from .serializers import WilayaSerializer, DairaSerializer


class WilayaViewSet(ListAPIView , RetrieveAPIView):
    queryset = Wilaya.objects.prefetch_related('dairas').all()
    serializer_class = WilayaSerializer
    lookup_field = 'id'

class DairaViewSet(ListAPIView, RetrieveAPIView):
    queryset = Daira.objects.all()
    serializer_class = DairaSerializer
    lookup_field = 'id'
