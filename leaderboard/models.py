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
        score += (30 - active_char.day) * 3
        score += active_char.intellect
        score += active_char.charm
        score += active_char.coding
        score += active_char.endurance
        score += active_char.money / 1000

        return score

    @classmethod
    def leaderboard_check(cls, active_char):
        """
        Checks if active character's score has reached the top 10.
        Sorts leaderboard and checks length to see if less than 10
        If more than 10 then compares to 9th entry and replaces if higher
        """

        leaderboard = Leaderboard.objects.all().order_by('-score')
        score = cls.calculate_score(active_char)

        if len(Leaderboard.objects.filter(
                user=active_char.user,
                score=score)) > 0:
            return False
        elif len(leaderboard) >= 10:
            if leaderboard[9].score > score:
                return False
            leaderboard[9].delete()
            cls.active_char_to_leaderboard(active_char, score)
            return True
        cls.active_char_to_leaderboard(active_char, score)
        return True
