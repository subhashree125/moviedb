from django.contrib import admin

from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'director', 'release_date', 'genre')
    search_fields = ('title', 'director')
    list_filter = ('genre', 'release_date')
admin.site.register(Movie, MovieAdmin)

fieldsets = (
    (None, {
        'fields': ('title', 'director', 'release_date', 'genre', 'description', 'poster')
    }),
)


# Register your models here.
