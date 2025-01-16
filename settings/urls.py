from django.urls import path
from settings.views import index, news

urlpatterns = [
    path("", index),
    path("news/", news)
]
