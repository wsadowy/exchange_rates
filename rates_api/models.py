from django.db import models


class CurrencyRate(models.Model):
    currency = models.CharField(max_length=30)
    rate = models.DecimalField(decimal_places=2, max_digits=8)
    rate_from = models.DateField()

    class Meta:
        verbose_name_plural = 'Currency Rates'
