from rest_framework import serializers


from .models import Wilaya, Daira


class DairaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Daira
        fields = ['name', 'ar_name', 'wilaya']
class WilayaSerializer(serializers.ModelSerializer):
    dairas = DairaSerializer(many=True)
    class Meta:
        model = Wilaya
        fields = ['name', 'ar_name', 'id', 'dairas']