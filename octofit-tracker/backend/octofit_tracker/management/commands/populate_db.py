from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    name = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    user = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    score = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    class Meta:
        app_label = 'octofit_tracker'

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete all data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='test'),
            User.objects.create_user(username='captainamerica', email='cap@marvel.com', password='test'),
            User.objects.create_user(username='batman', email='batman@dc.com', password='test'),
            User.objects.create_user(username='superman', email='superman@dc.com', password='test'),
        ]

        # Create activities
        Activity.objects.create(name='Run', user='ironman', team='Marvel')
        Activity.objects.create(name='Swim', user='captainamerica', team='Marvel')
        Activity.objects.create(name='Fly', user='superman', team='DC')
        Activity.objects.create(name='Detective Work', user='batman', team='DC')

        # Create leaderboard
        Leaderboard.objects.create(user='ironman', team='Marvel', score=100)
        Leaderboard.objects.create(user='captainamerica', team='Marvel', score=90)
        Leaderboard.objects.create(user='batman', team='DC', score=95)
        Leaderboard.objects.create(user='superman', team='DC', score=110)

        # Create workouts
        Workout.objects.create(name='Pushups', description='Do 50 pushups')
        Workout.objects.create(name='Situps', description='Do 50 situps')
        Workout.objects.create(name='Squats', description='Do 50 squats')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
