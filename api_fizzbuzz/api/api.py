from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializer import FizzBuzzSerializer
from .fizzbuzz import fizz_buzz


class FizzBuzzView(APIView):

    def get(self, request):
        if request.method == 'GET':
            numbers = str(fizz_buzz.fizz_buzz_dict(self).keys())
            fizzbuzz = str(fizz_buzz.fizz_buzz_dict(self).values())
            serializer = FizzBuzzSerializer(data={"numbers": numbers, "fizzbuzz":fizzbuzz})
            if not serializer.is_valid():
                return Response(serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)

            fizzbuzz = fizz_buzz.fizz_buzz_dict(self)


            return Response(fizzbuzz, status=status.HTTP_200_OK)