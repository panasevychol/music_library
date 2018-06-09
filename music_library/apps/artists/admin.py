from django.contrib import admin

from .models import Artist


class ArtistAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

# Register your models here.
admin.site.register(Artist, ArtistAdmin)
