from rest_framework import serializers

from rates_api.models import CurrencyRate


class RateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CurrencyRate
        fields = ('currency', 'rate', 'rate_from')
