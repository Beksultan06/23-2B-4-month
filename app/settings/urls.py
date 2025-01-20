from django.urls import path
from app.settings.views import index

urlpatterns = [
    path("", index, name='index')
]
