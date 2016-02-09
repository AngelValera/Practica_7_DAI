from django.contrib import admin
from app.models import Bar, Tapa

class BarAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('nombre',)}

class TapaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('nombre',)}

admin.site.register(Bar, BarAdmin)
admin.site.register(Tapa, TapaAdmin)
