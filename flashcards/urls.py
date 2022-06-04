from django.urls import path
from .views import CardsetListCreateView, CardsetDetailView

urlpatterns = [
    path('cardsets/', CardsetListCreateView.as_view()),
    path('cardsets/<int:cardset_id>/', CardsetDetailView.as_view())
]
