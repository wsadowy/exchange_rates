from rest_framework import viewsets

from rates_api.models import CurrencyRate
from rates_api.serializers import RateSerializer


class RateView(viewsets.ModelViewSet):
    queryset = CurrencyRate.objects.all()
    queryset.order_by('rate_from')
    serializer_class = RateSerializer
