from django.urls import path
from .views import CardsetListCreateView, CardsetDetailView, FlashcardListCreateView, FlashcardDetailView

urlpatterns = [
    path('cardsets/', CardsetListCreateView.as_view()),
    path('cardsets/<int:cardset_id>/', CardsetDetailView.as_view()),
    path('cardsets/<int:cardset_id>/cards/',
         FlashcardListCreateView.as_view()),
    path('cardsets/<int:cardset_id>/cards/<int:flashcard_id>/',
         FlashcardDetailView.as_view()),
]
