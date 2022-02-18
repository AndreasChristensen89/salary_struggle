from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField
from codex.models import Item


class Profile(models.Model):
    """
    Profile model to keep track of paid status,
    order history, and delivery information
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    active_char = models.BooleanField(default=False)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='Country', null=True, blank=True)

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
    money = models.IntegerField(default=20000)
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
        """
        Model class to create a character
        """

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
