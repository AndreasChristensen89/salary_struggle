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
        entry['char_intellect'] = active_char.current_level
        entry['char_charm'] = active_char.battle_count
        entry['char_coding'] = active_char.character_id
        entry['char_endurance'] = active_char.char_hp
        entry['char_money'] = active_char.char_attack
        entry['char_day'] = active_char.char_defense

        new_leaderboard_entry = cls(**entry)
        new_leaderboard_entry.save()
