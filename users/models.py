from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    SIXTH_GRADE = 6
    SEVENTH_GRADE = 7
    EIGHTH_GRADE = 8
    NINTH_GRADE = 9
    TENTH_GRADE = 10
    ELEVENTH_GRADE = 11
    TWELFTH_GRADE = 12
    GRADE_LEVEL_CHOICES = [
        (SIXTH_GRADE, "6th"),
        (SEVENTH_GRADE, "7th"),
        (EIGHTH_GRADE, "8th"),
        (NINTH_GRADE, "9th (Freshman)"),
        (TENTH_GRADE, "10th (Sophomore)"),
        (ELEVENTH_GRADE, "11th (Junior)"),
        (SIXTH_GRADE, "12th (Senior)"),
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
        max_length=2, choices=GRADE_LEVEL_CHOICES, default=SIXTH_GRADE
    )

    def __str__(self):
        return self.user.username
