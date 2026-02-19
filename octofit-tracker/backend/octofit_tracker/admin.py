from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'created_at']
    search_fields = ['username', 'email']
    readonly_fields = ['created_at']


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']
    readonly_fields = ['created_at']


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['activity_type', 'user_id', 'duration', 'calories', 'date']
    list_filter = ['activity_type', 'date']
    search_fields = ['user_id', 'activity_type']
    date_hierarchy = 'date'


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ['username', 'rank', 'total_calories', 'total_activities', 'updated_at']
    list_filter = ['updated_at']
    search_fields = ['username']
    ordering = ['rank']
    readonly_fields = ['updated_at']


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ['title', 'activity_type', 'difficulty', 'duration', 'calories_estimate']
    list_filter = ['activity_type', 'difficulty']
    search_fields = ['title', 'description']
    readonly_fields = ['created_at']
