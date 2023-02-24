from rest_framework import serializers


from .models import Wilaya, Daira

class WilayaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wilaya
        fields = ['name', 'ar_name', 'dairas']