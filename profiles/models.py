from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from codex.models import Item


class Profile(models.Model):
    """
    Profile model to keep track of paid status and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    active_char = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    @classmethod
    def remove_active_char(cls, user):
        """
        Model class to remove a character
        """
        cur_user = cls.objects.get(user=user)
        cur_user.active_char = False
        cur_user.save()


@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class ActiveCharacter(models.Model):
    """
    Character model
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    level = models.IntegerField(default=1)
    day = models.IntegerField(default=1)
    money = models.IntegerField(default=10000)
    intellect = models.IntegerField(default=1)
    charm = models.IntegerField(default=1)
    coding = models.IntegerField(default=1)
    endurance = models.IntegerField(default=1)
    energy = models.IntegerField(default=100)
    energy_penalty = models.IntegerField(default=0)
    has_job = models.BooleanField(default=False)
    items = models.ManyToManyField(Item, related_name='character_items',
                                   blank=True)

    def __str__(self):
        return f"{self.user.username} - Level {self.level}"

    @classmethod
    def create_new_character(cls, user):
        """
        Model class to create a character
        """

        # Update character in case there is a character to replace
        if ActiveCharacter.objects.filter(user=user).exists():
            ActiveCharacter.objects.filter(user=user).delete()

        # Create ActiveCharacter object and save
        new_character = {}
        new_character["user"] = user

        entry = cls(**new_character)
        entry.save()

        # Update profile to set active character
        user_profile = Profile.objects.get(user=user)
        user_profile.active_char = True
        user_profile.save()

        return entry
