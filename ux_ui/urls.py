from django.urls import path
from ux_ui.views import ux_ui

urlpatterns = [
    path("ux_ui", ux_ui)
]
