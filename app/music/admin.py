from django.contrib import admin
from .models import Performer, Album, Song


class SongAdmin(admin.ModelAdmin):
    list_display = ('name', 'performer', 'album',  'position', )
    list_filter = ('name', )



admin.site.register(Performer)
admin.site.register(Album)
admin.site.register(Song, SongAdmin)