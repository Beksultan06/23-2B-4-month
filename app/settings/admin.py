from django.contrib import admin
from app.settings.models import Settings, Info, About, AboutMe, Works, Contact
# Register your models here.
admin.site.register(Settings)
admin.site.register(Info)
admin.site.register(About)
admin.site.register(Works)
admin.site.register(Contact)

@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ['id', 'key', 'value']
    list_filter = ['id', 'key', 'value']
    search_fields = ['id', 'key', 'value']