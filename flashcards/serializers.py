from .models import Cardset, Flashcard
from rest_framework import serializers


# TODO: Add 'username' field to owner object
class CardsetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cardset
        fields = ('id', 'title', 'owner', 'flashcard_count')


class FlashcardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flashcard
        fields = ('id', 'question', 'answer', 'cardset')
