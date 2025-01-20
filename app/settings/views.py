from django.shortcuts import render
from app.settings.models import Settings, Info, About

def index(request):
    settings_id = Settings.objects.latest("id")
    info_all = Info.objects.all()
    about = About.objects.latest("id")
    return render(request, "index.html", locals())