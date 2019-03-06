from django.urls import include, path
from rest_framework import routers

from rates_api import views

router = routers.DefaultRouter()
router.register('currencies', views.RateView)


urlpatterns = [
    path('', include(router.urls))
]
