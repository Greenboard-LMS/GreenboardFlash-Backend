from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Cardset, Flashcard
from .serializers import CardsetSerializer, FlashcardSerializer
from django.core.exceptions import ObjectDoesNotExist


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
    # TODO: Updating a cardset
    permission_classes = (IsAuthenticated,)

    def get(self, request, cardset_id):
        queryset = Cardset.objects.get(id=cardset_id)
        serializer = CardsetSerializer(queryset)
        return Response(serializer.data)


class FlashcardListCreateView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, cardset_id):
        queryset = Flashcard.objects.all().filter(cardset__id=cardset_id)
        serializer = FlashcardSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, cardset_id):
        serializer = FlashcardSerializer(data=request.data, context={
                                         'cardset_id': cardset_id})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class FlashcardDetailView(APIView):
    # TODO: Updating a Flashcard
    permission_classes = (IsAuthenticated,)

    def get(self, request, cardset_id, flashcard_id):
        # TODO: Also take cardset into consideration
        try:
            queryset = Cardset.objects.get(
                id=cardset_id).flashcard_set.get(id=flashcard_id)
            serializer = FlashcardSerializer(queryset)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response({'error': 'Flashcard does not exist'})
