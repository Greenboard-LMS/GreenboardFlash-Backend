from django.urls import path
from .views import CardsetListView, CardsetDetailView

urlpatterns = [
    path('cardsets/', CardsetListView.as_view()),
    path('cardsets/<int:cardset_id>/', CardsetDetailView.as_view())
]
