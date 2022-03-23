from django.db import models
from django.contrib.auth.models import User


class Leaderboard(models.Model):
    """
    Leaderboard Model for entries of finished games
    Takes in active character's stats, checks for top 10,
    if ok adds the score
    """

    class Meta:
        """
        Specify plural name in admin
        """
        verbose_name_plural = 'Leaderboard'

    user = models.ForeignKey(User, on_delete=models.SET_NULL,
                             blank=False, null=True)
    score = models.IntegerField(null=False, blank=False)
    submission_date = models.DateTimeField(auto_now_add=True)
    char_intellect = models.IntegerField(null=False, blank=False)
    char_charm = models.IntegerField(null=False, blank=False)
    char_coding = models.IntegerField(null=False, blank=False)
    char_endurance = models.IntegerField(null=False, blank=False)
    char_money = models.IntegerField(null=False, blank=False)
    char_day = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return f'{self.user.username} | Day {self.char_day }'

    @classmethod
    def active_char_to_leaderboard(cls, active_char, score):
        """
        Class method that creates an entry to be added
        Takes in the active character and the score to build entry
        """

        entry = {}
        entry['user'] = active_char.user
        entry['char_intellect'] = active_char.intellect
        entry['char_charm'] = active_char.charm
        entry['char_coding'] = active_char.coding
        entry['char_endurance'] = active_char.endurance
        entry['char_money'] = active_char.money
        entry['char_day'] = active_char.day
        entry['score'] = score

        new_leaderboard_entry = cls(**entry)
        new_leaderboard_entry.save()

    @staticmethod
    def calculate_score(active_char):
        """
        Calculates score of active character
        Uses stats and combines them into one number
        """
        score = 0
        score += active_char.day
        score += active_char.intellect
        score += active_char.charm
        score += active_char.coding
        score += active_char.endurance

        return score

    @classmethod
    def leaderboard_check(cls, active_char):
        """
        Checks if active character's score has reached the top 10.
        Sorts leaderboard and checks length to see if less than 10
        If more than 10 then compares to 9th entry and replaces if higher
        """

        current_leaderboard = cls.objects.sort_leaderboard()
        score = cls.calculate_score(active_char)

        if len(current_leaderboard) >= 10:
            if current_leaderboard[9].score > score:
                return (False, score)
            current_leaderboard[9].delete()
            cls.active_char_to_leaderboard(active_char, score)
            return (True, score)
        cls.active_char_to_leaderboard(active_char, score)
        return (True, score)
