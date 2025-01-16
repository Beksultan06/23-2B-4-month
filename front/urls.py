from django.urls import path
from front.views import front

urlpatterns = [
    path("front", front)
]
