from django.contrib import admin

from .models import Mineral


class MineralAdmin(admin.ModelAdmin):
    inlines = []

admin.site.register(Mineral, MineralAdmin)
