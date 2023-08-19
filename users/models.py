from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    GRADE_LEVEL_CHOICES = [
        ("6", "6th"),
        ("7", "7th"),
        ("8", "8th"),
        ("9", "9th (Freshman)"),
        ("10", "10th (Sophomore)"),
        ("11", "11th (Junior)"),
        ("12", "12th (Senior)"),
    ]
    CAREER_INTERESTS_CHOICES = [
        ("Healthcare", "Healthcare and Medicine"),
        ("Arts", "Arts and Creativity"),
        ("Business", "Business and Entrepreneurship"),
        ("Social_Sciences", "Social Sciences"),
        ("Education", "Education and Teaching"),
        ("Engineering", "Engineering and Design"),
        ("Environmental", "Environmental and Sustainability"),
        ("Communication", "Communication and Media"),
        ("Culinary", "Culinary and Hospitality"),
        ("Law", "Law and Justice"),
        ("Sports", "Sports and Fitness"),
        ("Technology", "Technology and IT"),
        ("Trades", "Skilled Trades"),
        ("Fashion", "Fashion and Design"),
        ("Agriculture", "Agriculture and Farming"),
        ("Writing", "Writing and Publishing"),
        ("Research", "Research and Academia"),
        ("Undecided", "Undecided"),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    career_interest = models.CharField(
        max_length=200, choices=CAREER_INTERESTS_CHOICES, default="Undecided"
    )
    grade_level = models.CharField(
        max_length=200, choices=GRADE_LEVEL_CHOICES, null=True
    )

    def __str__(self):
        return self.user.username
