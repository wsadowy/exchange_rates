from rest_framework import viewsets

from rates_api.models import CurrencyRate
from rates_api.serializers import RateSerializer


class RateView(viewsets.ModelViewSet):
    queryset = CurrencyRate.objects.all()
    serializer_class = RateSerializer
