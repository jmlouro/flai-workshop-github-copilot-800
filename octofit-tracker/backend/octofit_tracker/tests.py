from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from .models import User, Team, Activity, Leaderboard, Workout
from datetime import datetime


class UserModelTest(TestCase):
    """Test User model"""

    def setUp(self):
        self.user = User.objects.create(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

    def test_user_creation(self):
        """Test that a user can be created"""
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertIsNotNone(self.user._id)

    def test_user_string_representation(self):
        """Test the string representation of a user"""
        self.assertEqual(str(self.user), 'testuser')


class TeamModelTest(TestCase):
    """Test Team model"""

    def setUp(self):
        self.team = Team.objects.create(
            name='Test Team',
            description='A test team'
        )

    def test_team_creation(self):
        """Test that a team can be created"""
        self.assertEqual(self.team.name, 'Test Team')
        self.assertEqual(self.team.description, 'A test team')
        self.assertIsNotNone(self.team._id)

    def test_team_string_representation(self):
        """Test the string representation of a team"""
        self.assertEqual(str(self.team), 'Test Team')


class ActivityModelTest(TestCase):
    """Test Activity model"""

    def setUp(self):
        self.activity = Activity.objects.create(
            user_id='507f1f77bcf86cd799439011',
            activity_type='Running',
            duration=30,
            distance=5.0,
            calories=300,
            date=datetime.now()
        )

    def test_activity_creation(self):
        """Test that an activity can be created"""
        self.assertEqual(self.activity.activity_type, 'Running')
        self.assertEqual(self.activity.duration, 30)
        self.assertEqual(self.activity.calories, 300)
        self.assertIsNotNone(self.activity._id)


class LeaderboardModelTest(TestCase):
    """Test Leaderboard model"""

    def setUp(self):
        self.leaderboard = Leaderboard.objects.create(
            user_id='507f1f77bcf86cd799439011',
            username='testuser',
            total_calories=1000,
            total_activities=10,
            rank=1
        )

    def test_leaderboard_creation(self):
        """Test that a leaderboard entry can be created"""
        self.assertEqual(self.leaderboard.username, 'testuser')
        self.assertEqual(self.leaderboard.total_calories, 1000)
        self.assertEqual(self.leaderboard.rank, 1)


class WorkoutModelTest(TestCase):
    """Test Workout model"""

    def setUp(self):
        self.workout = Workout.objects.create(
            title='Morning Run',
            description='A refreshing morning run',
            activity_type='Running',
            difficulty='Medium',
            duration=30,
            calories_estimate=300
        )

    def test_workout_creation(self):
        """Test that a workout can be created"""
        self.assertEqual(self.workout.title, 'Morning Run')
        self.assertEqual(self.workout.difficulty, 'Medium')
        self.assertEqual(self.workout.calories_estimate, 300)


class APIRootTest(APITestCase):
    """Test API root endpoint"""

    def test_api_root(self):
        """Test that API root returns correct links"""
        url = reverse('api-root')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('users', response.data)
        self.assertIn('teams', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('leaderboard', response.data)
        self.assertIn('workouts', response.data)


class UserAPITest(APITestCase):
    """Test User API endpoints"""

    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpass123'
        }

    def test_create_user(self):
        """Test creating a user via API"""
        url = reverse('user-list')
        response = self.client.post(url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testuser')

    def test_get_users(self):
        """Test retrieving users via API"""
        User.objects.create(**self.user_data)
        url = reverse('user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class TeamAPITest(APITestCase):
    """Test Team API endpoints"""

    def setUp(self):
        self.client = APIClient()
        self.team_data = {
            'name': 'Test Team',
            'description': 'A test team',
            'members': []
        }

    def test_create_team(self):
        """Test creating a team via API"""
        url = reverse('team-list')
        response = self.client.post(url, self.team_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Team.objects.count(), 1)


class ActivityAPITest(APITestCase):
    """Test Activity API endpoints"""

    def setUp(self):
        self.client = APIClient()
        self.activity_data = {
            'user_id': '507f1f77bcf86cd799439011',
            'activity_type': 'Running',
            'duration': 30,
            'distance': 5.0,
            'calories': 300,
            'date': datetime.now().isoformat(),
            'notes': 'Great run!'
        }

    def test_create_activity(self):
        """Test creating an activity via API"""
        url = reverse('activity-list')
        response = self.client.post(url, self.activity_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Activity.objects.count(), 1)
