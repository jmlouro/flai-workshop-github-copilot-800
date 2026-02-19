from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId


class UserSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'created_at']
        extra_kwargs = {'password': {'write_only': True}}

    def get_id(self, obj):
        """Convert ObjectId to string"""
        return str(obj._id) if hasattr(obj, '_id') and obj._id else None

    def create(self, validated_data):
        user = User(**validated_data)
        user.save()
        return user


class TeamSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'created_at', 'members']

    def get_id(self, obj):
        """Convert ObjectId to string"""
        return str(obj._id) if hasattr(obj, '_id') and obj._id else None


class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = Activity
        fields = ['id', 'user_id', 'activity_type', 'duration', 'distance', 'calories', 'date', 'notes']

    def get_id(self, obj):
        """Convert ObjectId to string"""
        return str(obj._id) if hasattr(obj, '_id') and obj._id else None


class LeaderboardSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = Leaderboard
        fields = ['id', 'user_id', 'username', 'total_calories', 'total_activities', 'rank', 'updated_at']

    def get_id(self, obj):
        """Convert ObjectId to string"""
        return str(obj._id) if hasattr(obj, '_id') and obj._id else None


class WorkoutSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = Workout
        fields = ['id', 'title', 'description', 'activity_type', 'difficulty', 'duration', 'calories_estimate', 'created_at']

    def get_id(self, obj):
        """Convert ObjectId to string"""
        return str(obj._id) if hasattr(obj, '_id') and obj._id else None
