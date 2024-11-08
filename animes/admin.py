from django.contrib import admin
from animes.models import Animes


@admin.register(Animes)
class AnimesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'release_date')
