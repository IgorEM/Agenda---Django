from django.contrib import admin
from core.models import Evento #importou de core.models (o caminho) a class Evento

# Register your models here.

class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_evento', 'data_criacao') #para aparecer essas opçoes na listagem
    list_filter = ('titulo','usuario','data_evento') #cria filtros do lado direito
admin.site.register(Evento, EventoAdmin)
