from django.contrib import admin
from app.settings.models import Settings, Info
# Register your models here.
admin.site.register(Settings)
admin.site.register(Info)
