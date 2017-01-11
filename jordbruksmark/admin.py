# -*- coding: utf-8 -*-

from django.contrib import admin, messages
from jordbruksmark.models import *

class ParzellenAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "name"]
    search_fields = ["id", "code", "name"]
    
class DuengungsstufenAdmin(admin.ModelAdmin):
    list_display = ["__unicode__"]
    search_fields = ["id", "name"]
    
class DuengerAdmin(admin.ModelAdmin):
    list_display = ["__unicode__"]
    search_fields = ["id", "name"]
    
class FamilienAdmin(admin.ModelAdmin):
    list_display = ["__unicode__"]
    search_fields = ["id", "name"]
    
class KulturenAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "familie_name"]
    search_fields = ["id", "name", "familie__name"]
    def familie_name(self, obj):
        return obj.familie.name
    familie_name.admin_order_field = 'familie__name'
    
class WochenMengenAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "menge"]
    search_fields = ["id", "woche", "kultur__name"]
    
class SaetzeAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "sorte"]
    search_fields = ["id", "sorte", "kultur__name", "nummer"]

admin.site.register(Parzelle, ParzellenAdmin)
admin.site.register(Duengungsstufe, DuengungsstufenAdmin)
admin.site.register(Duenger, DuengerAdmin)
admin.site.register(Familie, FamilienAdmin)
admin.site.register(Kultur, KulturenAdmin)
admin.site.register(WochenMenge, WochenMengenAdmin)
admin.site.register(Satz,SaetzeAdmin)
