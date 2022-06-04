from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Cardset
from .serializers import CardsetSerializer


class CardsetListCreateView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        queryset = Cardset.objects.all()
        serializer = CardsetSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        # TODO: Add something like "pre_save" so that owner field is automatically set to the requesting user
        serializer = CardsetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class CardsetDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, cardset_id):
        queryset = Cardset.objects.get(id=cardset_id)
        serializer = CardsetSerializer(queryset)
        return Response(serializer.data)
