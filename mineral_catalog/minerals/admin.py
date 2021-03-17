from django.contrib import admin

from .models import Mineral, Attribute


class AttributeInline(admin.StackedInline):
    model = Attribute


class MineralAdmin(admin.ModelAdmin):
    inlines = [AttributeInline,]

admin.site.register(Mineral, MineralAdmin)
admin.site.register(Attribute)
