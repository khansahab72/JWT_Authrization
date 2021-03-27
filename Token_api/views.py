from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  # <--here


# Create your views here.
class FirstApi(APIView):
    permission_classes = (IsAuthenticated,)  # <-- to here

    def get(self, request):
        content = {'Api': 'this is my first API!'}
        return Response(content)
