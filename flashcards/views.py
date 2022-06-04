from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Cardset
from .serializers import CardsetSerializer


class CardsetListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Cardset.objects.all()
    serializer_class = CardsetSerializer


class CardsetDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, cardset_id):
        queryset = Cardset.objects.get(id=cardset_id)
        serializer = CardsetSerializer(queryset)
        return Response(serializer.data)
