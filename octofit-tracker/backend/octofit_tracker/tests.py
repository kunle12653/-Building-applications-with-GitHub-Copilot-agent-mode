from django.test import TestCase
from django.contrib.auth.models import User
from .models import Team, Activity, Leaderboard, Workout

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name="Test Team")
        self.assertEqual(str(team), "Test Team")

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(name="Run", user="user1", team="Test Team")
        self.assertEqual(str(activity), "Run - user1")

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        leaderboard = Leaderboard.objects.create(user="user1", team="Test Team", score=100)
        self.assertEqual(str(leaderboard), "user1 - 100")

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name="Pushups", description="Do 20 pushups")
        self.assertEqual(str(workout), "Pushups")