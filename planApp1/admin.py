from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Abteilung)
admin.site.register(Ausbildungsberuf)
admin.site.register(Lernfeld)
admin.site.register(Schlagwort)
#admin.site.register(Lernbaustein)
@admin.register(Lernbaustein)
class LernbausteinAdmin(admin.ModelAdmin):
    # list_display = ['name']
    list_filter = ['lernfeld__berufe__abteilung', 'lernfeld__berufe', 'schlagwoerter'] 
    search_fields = ['beschreibung']