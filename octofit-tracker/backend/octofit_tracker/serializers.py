from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Team, Activity, Leaderboard, Workout
from bson import ObjectId

class ObjectIdField(serializers.Field):
    def to_representation(self, value):
        return str(value)
    def to_internal_value(self, data):
        return ObjectId(data)

class UserSerializer(serializers.ModelSerializer):
    id = ObjectIdField(source='_id', read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class TeamSerializer(serializers.ModelSerializer):
    id = ObjectIdField(source='_id', read_only=True)
    class Meta:
        model = Team
        fields = ['id', 'name']

class ActivitySerializer(serializers.ModelSerializer):
    id = ObjectIdField(source='_id', read_only=True)
    class Meta:
        model = Activity
        fields = ['id', 'name', 'user', 'team']

class LeaderboardSerializer(serializers.ModelSerializer):
    id = ObjectIdField(source='_id', read_only=True)
    class Meta:
        model = Leaderboard
        fields = ['id', 'user', 'team', 'score']

class WorkoutSerializer(serializers.ModelSerializer):
    id = ObjectIdField(source='_id', read_only=True)
    class Meta:
        model = Workout
        fields = ['id', 'name', 'description']
