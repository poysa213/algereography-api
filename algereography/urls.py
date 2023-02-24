from .views import WilayaViewSet, DairaViewSet
from django.urls import path


urlpatterns = [
    path('wilaya', WilayaViewSet.as_view(), name="wilaya"),
    path('wilaya/<int:id>/', WilayaViewSet.as_view(), name='wilaya_detail'),
    path('daira', DairaViewSet.as_view(), name="daira"),
    path('daira/<int:id>/', DairaViewSet.as_view(), name='daira_detail'),
]
