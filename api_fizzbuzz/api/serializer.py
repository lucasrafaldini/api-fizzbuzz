from rest_framework import serializers


class FizzBuzzSerializer(serializers.Serializer):
    numbers = serializers.CharField(max_length=1000)
    fizzbuzz = serializers.CharField(max_length=1000)