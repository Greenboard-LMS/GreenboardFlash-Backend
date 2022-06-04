from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Cardset
from .serializers import CardsetSerializer


class CardsetListView(APIView):
    def get(self, request):
        queryset = Cardset.objects.all()
        serializer = CardsetSerializer(queryset, many=True)
        return Response(serializer.data)
