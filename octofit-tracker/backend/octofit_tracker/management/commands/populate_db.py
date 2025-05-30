from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient
from datetime import timedelta
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB（必ずlocalhost:27017を使用）
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create users
        users = [
            {"_id": ObjectId(), "email": "thundergod@mhigh.edu", "name": "thundergod", "password": "thundergodpassword"},
            {"_id": ObjectId(), "email": "metalgeek@mhigh.edu", "name": "metalgeek", "password": "metalgeekpassword"},
            {"_id": ObjectId(), "email": "zerocool@mhigh.edu", "name": "zerocool", "password": "zerocoolpassword"},
            {"_id": ObjectId(), "email": "crashoverride@hmhigh.edu", "name": "crashoverride", "password": "crashoverridepassword"},
            {"_id": ObjectId(), "email": "sleeptoken@mhigh.edu", "name": "sleeptoken", "password": "sleeptokenpassword"},
        ]
        db.users.insert_many(users)

        # Create teams
        blue_team = {"_id": ObjectId(), "name": "Blue Team", "members": [users[0]["_id"], users[1]["_id"], users[2]["_id"]]}
        gold_team = {"_id": ObjectId(), "name": "Gold Team", "members": [users[3]["_id"], users[4]["_id"]]}
        db.teams.insert_many([blue_team, gold_team])

        # Create activities
        activities = [
            {"_id": ObjectId(), "user": users[0]["_id"], "activity_type": "Cycling", "duration": 60, "date": "2025-05-30T10:00:00Z"},
            {"_id": ObjectId(), "user": users[1]["_id"], "activity_type": "Crossfit", "duration": 120, "date": "2025-05-30T11:00:00Z"},
            {"_id": ObjectId(), "user": users[2]["_id"], "activity_type": "Running", "duration": 90, "date": "2025-05-30T12:00:00Z"},
            {"_id": ObjectId(), "user": users[3]["_id"], "activity_type": "Strength", "duration": 30, "date": "2025-05-30T13:00:00Z"},
            {"_id": ObjectId(), "user": users[4]["_id"], "activity_type": "Swimming", "duration": 75, "date": "2025-05-30T14:00:00Z"},
        ]
        db.activity.insert_many(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            {"_id": ObjectId(), "team": blue_team["_id"], "points": 100},
            {"_id": ObjectId(), "team": gold_team["_id"], "points": 90},
        ]
        db.leaderboard.insert_many(leaderboard_entries)

        # Create workouts
        workouts = [
            {"_id": ObjectId(), "user": users[0]["_id"], "workout_type": "Cycling Training", "details": "Training for a road cycling event", "date": "2025-05-30T15:00:00Z"},
            {"_id": ObjectId(), "user": users[1]["_id"], "workout_type": "Crossfit", "details": "Training for a crossfit competition", "date": "2025-05-30T16:00:00Z"},
            {"_id": ObjectId(), "user": users[2]["_id"], "workout_type": "Running Training", "details": "Training for a marathon", "date": "2025-05-30T17:00:00Z"},
            {"_id": ObjectId(), "user": users[3]["_id"], "workout_type": "Strength Training", "details": "Training for strength", "date": "2025-05-30T18:00:00Z"},
            {"_id": ObjectId(), "user": users[4]["_id"], "workout_type": "Swimming Training", "details": "Training for a swimming competition", "date": "2025-05-30T19:00:00Z"},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
