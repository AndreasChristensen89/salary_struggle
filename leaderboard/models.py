from django.db import models
from django.contrib.auth.models import User


class Leaderboard(models.Model):
    """
    Leaderboard Model
    """

    class Meta:
        """
        Specify plural name in admin
        """
        verbose_name_plural = 'Leaderboard'

    user = models.ForeignKey(User, on_delete=models.SET_NULL,
                             blank=False, null=True)
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
    def active_char_to_leaderboard(cls, active_char):
        """
        Class method for building the required structure of
        the leaderboard model before saving it to the database.
        Method takes in active character and their score.
        """

        entry = {}
        entry['user'] = active_char.user
        entry['char_intellect'] = active_char.intellect
        entry['char_charm'] = active_char.charm
        entry['char_coding'] = active_char.coding
        entry['char_endurance'] = active_char.endurance
        entry['char_money'] = active_char.money
        entry['char_day'] = active_char.day

        new_leaderboard_entry = cls(**entry)
        new_leaderboard_entry.save()

    @staticmethod
    def calculate_score(active_char):
        """
        Static method for calculating the score of an active
        player. Used for comparing entries within the database,
        and for saving new entry to the DB.
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
        Class method for checking whether active character
        has earned a place on the scoreboard.
        Method obtains all current entries in leaderboard
        DB, calculates users score, and determines whether
        the active characters score is higher than the lowest
        entry in the DB. If so, or if there are less than 10
        entries in the DB, the method calls the active_char_to_leaderboard
        method to store the active character and their score to the DB.
        Returns Bool to confirm if score has been entered, and players score.
        """

        current_leaderboard = cls.objects.sort_leaderboard()
        score = cls.calculate_score(active_char)

        if len(current_leaderboard) >= 10:
            if current_leaderboard[9].score > score:
                return (False, score)
            current_leaderboard[9].delete()
            cls.active_char_to_leaderboard(active_char)
            return (True, score)
        cls.active_char_to_leaderboard(active_char)
        return (True, score)
