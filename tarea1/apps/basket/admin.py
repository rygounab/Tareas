from django.contrib import admin

from apps.basket.models import Team, Player, Coach, Match

# Register your models here.
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display=('name', 'description', 'logo', 'code')
    search_fields = ('name',)

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display=('name','nickname','birthh_date','age_old','rut','email','height','weight','photo','positionGame')
    search_fields = ('name', 'nickname','rut')
    list_filter=('team','birthh_date')

@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display=('name','age_old','email','rut','nickname')
    list_filter=('team',)

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display=('name','equipos')
    list_filter=('teams',)
