from djongo import models


class User(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=100, unique=True, blank=True, null=True)
    superhero_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    team_id = models.CharField(max_length=100, blank=True, null=True)
    avatar = models.CharField(max_length=10, blank=True, null=True)
    total_points = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.name or self.username or self.email


class Team(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    members = models.JSONField(default=list)  # List of user IDs

    class Meta:
        db_table = 'teams'

    def __str__(self):
        return self.name


class Activity(models.Model):
    _id = models.ObjectIdField()
    user_id = models.CharField(max_length=24)  # ObjectId as string
    workout_id = models.CharField(max_length=50, blank=True, null=True)
    activity_type = models.CharField(max_length=50)
    duration_minutes = models.IntegerField(null=True, blank=True)  # in minutes
    distance = models.FloatField(null=True, blank=True)  # in km
    calories_burned = models.IntegerField(null=True, blank=True)
    points_earned = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField()
    notes = models.TextField(blank=True)

    class Meta:
        db_table = 'activities'

    def __str__(self):
        return f"{self.activity_type} - {self.date}"


class Leaderboard(models.Model):
    _id = models.ObjectIdField()
    user_id = models.CharField(max_length=24)  # ObjectId as string
    username = models.CharField(max_length=100)
    total_calories = models.IntegerField(default=0)
    total_activities = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'leaderboard'
        ordering = ['-total_calories']

    def __str__(self):
        return f"{self.username} - Rank {self.rank}"


class Workout(models.Model):
    _id = models.ObjectIdField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    activity_type = models.CharField(max_length=50)
    difficulty = models.CharField(max_length=20)  # Easy, Medium, Hard
    duration = models.IntegerField()  # in minutes
    calories_estimate = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'workouts'

    def __str__(self):
        return self.title
