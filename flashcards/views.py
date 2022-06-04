from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response

from .models import Cardset
from .serializers import CardsetSerializer


class CardsetListView(generics.ListCreateAPIView):
    queryset = Cardset.objects.all()
    serializer_class = CardsetSerializer


class CardsetDetailView(APIView):
    def get(self, request, cardset_id):
        queryset = Cardset.objects.get(id=cardset_id)
        serializer = CardsetSerializer(queryset)
        return Response(serializer.data)
