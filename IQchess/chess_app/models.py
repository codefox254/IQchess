from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=1200)  # Default chess rating

    def __str__(self):
        return self.user.username

class Chessbot(models.Model):
    LEVEL_CHOICES = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    ]
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    skill = models.IntegerField()  # This could determine the difficulty level

    def __str__(self):
        return self.level

class Game(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    chessbot = models.ForeignKey(Chessbot, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    moves = models.JSONField()  # Store moves as JSON for flexibility
    result = models.CharField(max_length=10, null=True, blank=True)  # e.g., 1-0, 0-1, 1/2-1/2

    def __str__(self):
        return f"Game by {self.player.username} against {self.chessbot.level}"

class Move(models.Model):
    game = models.ForeignKey(Game, related_name='game_moves', on_delete=models.CASCADE)  # Renamed related_name
    move_number = models.IntegerField()
    move_notation = models.CharField(max_length=10)  # e.g., e4, Nf3, etc.
    is_correct = models.BooleanField(default=True)
    feedback = models.TextField(null=True, blank=True)  # Feedback from the chessbot coach

    def __str__(self):
        return f"Move {self.move_number}: {self.move_notation} for Game {self.game.id}"

class Analysis(models.Model):
    game = models.ForeignKey(Game, related_name='analysis', on_delete=models.CASCADE)
    move = models.ForeignKey(Move, related_name='move_analysis', on_delete=models.CASCADE)  # Renamed related_name
    analysis_data = models.JSONField()  # Store analysis data as JSON

    def __str__(self):
        return f"Analysis for Move {self.move.id} in Game {self.game.id}"
