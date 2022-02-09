from django.db import models
from django.contrib.auth.models import User
from codex.models import Item


class Profile(models.Model):
    """
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    active_char = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    @classmethod
    def remove_active_char(cls, user):
        cur_user = cls.objects.get(user=user)
        cur_user.active_char = False
        cur_user.save()


class ActiveCharacter(models.Model):
    """
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    level = models.IntegerField(default=1)
    char_intellect = models.IntegerField(default=1)
    char_charm = models.IntegerField(default=1)
    char_coding = models.IntegerField(default=1)
    char_endurace = models.IntegerField(default=1)
    has_job = models.BooleanField(default=False)
    item_id = models.ForeignKey(Item, null=True, blank=True,
                                on_delete=models.CASCADE,
                                related_name="item")
    item_intellect = models.IntegerField(null=True, blank=True)
    item_charm = models.IntegerField(null=True, blank=True)
    item_coding = models.IntegerField(null=True, blank=True)
    item_endurance = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - Level {self.level}"

    @classmethod
    def create_character(cls, user):

        new_character = {}
        new_character["user"] = user

        # Create ActiveCharacter object and save
        entry = cls(**new_character)
        entry.save()

        # Update user profile to reflect new character
        user_profile = Profile.objects.get(user=user)
        user_profile.active_char = True
        user_profile.save()

        return entry
