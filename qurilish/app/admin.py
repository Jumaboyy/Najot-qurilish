from django.contrib import admin
from .models import Hudud, QurilishTashkiloti, QurilishBinisi

@admin.register(Hudud)
class HududAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(QurilishTashkiloti)
class QurilishTashkilotiAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'qachon_tashkil_topgan', 'hudud')
    search_fields = ('name', 'description')
    list_filter = ('hudud', 'qachon_tashkil_topgan')

@admin.register(QurilishBinisi)
class QurilishBinisiAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'qurilish_tashkiloti', 'hudud', 'maydoni', 'qavat', 'parkovka', 'bolalar_maydonchasi', 'lift')
    search_fields = ('name', 'qurilish_tashkiloti__name', 'hudud__name')
    list_filter = ('hudud', 'qurilish_tashkiloti', 'qavat', 'parkovka', 'bolalar_maydonchasi', 'lift')
