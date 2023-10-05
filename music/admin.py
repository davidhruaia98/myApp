from django.contrib import admin
from music.models import Album
from music.models import Song

admin.site.register(Album)


# Register your models here.
class SongAdmin(admin.ModelAdmin):
    list_display = ('song_title', 'album', 'file_type', 'is_favourite')


admin.site.register(Song, SongAdmin)
# Register your models here.
