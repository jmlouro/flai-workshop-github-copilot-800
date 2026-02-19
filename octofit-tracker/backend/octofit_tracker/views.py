from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import (
    UserSerializer, TeamSerializer, ActivitySerializer,
    LeaderboardSerializer, WorkoutSerializer
)


@api_view(['GET'])
def api_root(request, format=None):
    """
    API root endpoint that provides links to all available endpoints
    """
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'teams': reverse('team-list', request=request, format=format),
        'activities': reverse('activity-list', request=request, format=format),
        'leaderboard': reverse('leaderboard-list', request=request, format=format),
        'workouts': reverse('workout-list', request=request, format=format),
    })


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint for users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint for teams
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    """
    API endpoint for activities
    """
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    def get_queryset(self):
        """
        Optionally filter activities by user_id
        """
        queryset = Activity.objects.all()
        user_id = self.request.query_params.get('user_id', None)
        if user_id is not None:
            queryset = queryset.filter(user_id=user_id)
        return queryset


class LeaderboardViewSet(viewsets.ModelViewSet):
    """
    API endpoint for leaderboard
    """
    queryset = Leaderboard.objects.all().order_by('-total_calories')
    serializer_class = LeaderboardSerializer


class WorkoutViewSet(viewsets.ModelViewSet):
    """
    API endpoint for workout suggestions
    """
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

    def get_queryset(self):
        """
        Optionally filter workouts by activity_type or difficulty
        """
        queryset = Workout.objects.all()
        activity_type = self.request.query_params.get('activity_type', None)
        difficulty = self.request.query_params.get('difficulty', None)
        
        if activity_type is not None:
            queryset = queryset.filter(activity_type=activity_type)
        if difficulty is not None:
            queryset = queryset.filter(difficulty=difficulty)
        
        return queryset
