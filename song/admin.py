from django.contrib import admin
from .models import Song,Artist,Movies
# Register your models here.
admin.site.register(Song)
admin.site.register(Artist)
admin.site.register(Movies)
