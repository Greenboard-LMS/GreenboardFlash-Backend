
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('flash/', include('flashcards.urls')),
    path('users/', include('users.urls')),
]
