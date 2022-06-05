from .models import Cardset, Flashcard, Studyplan
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


class StudyplanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Studyplan
        fields = ('id', 'title', 'deadline', 'owner', 'cardsets_to_study')
