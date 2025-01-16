from django.urls import path
from back.views import back

urlpatterns = [
    path("back", back)
]
