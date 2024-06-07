from django.contrib import admin

from apps.galeria.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda', 'categoria', 'data_fotografia', 'publicada')
    list_display_links = ('id', 'nome', 'legenda', 'categoria', 'data_fotografia')
    search_fields = ('nome',)
    list_filter = ('categoria', 'usuario')
    list_editable = ('publicada', )
    list_per_page = 10

# Register your models here.
admin.site.register(Fotografia, ListandoFotografias)