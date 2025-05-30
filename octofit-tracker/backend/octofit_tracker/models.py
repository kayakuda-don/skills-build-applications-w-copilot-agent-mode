from djongo import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=128)
    # 他の必要なフィールド
    def __str__(self):
        return self.email

class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.JSONField(default=list)  # ArrayFieldからJSONFieldに変更
    # 他の必要なフィールド
    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=50)
    duration = models.IntegerField()
    date = models.DateTimeField()
    # 他の必要なフィールド

class Leaderboard(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.IntegerField()
    # 他の必要なフィールド

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workout_type = models.CharField(max_length=50)
    details = models.TextField()
    date = models.DateTimeField()
    # 他の必要なフィールド
