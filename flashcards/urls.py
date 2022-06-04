from django.urls import path
from .views import CardsetListView

urlpatterns = [
    path('cardsets/', CardsetListView.as_view())
]
