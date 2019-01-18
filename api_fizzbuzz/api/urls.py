from django.urls import path
from .api import FizzBuzzView


urlpatterns = [
    path('', FizzBuzzView.as_view(), name='fizzbuzz'),
]