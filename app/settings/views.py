from django.shortcuts import render
from app.settings.models import Settings, Info

def index(request):
    settings_id = Settings.objects.latest("id")
    info_all = Info.objects.all()
    return render(request, "index.html", locals())