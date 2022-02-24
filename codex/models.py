from django.db import models


class Interviewer(models.Model):
    """
    Model for the interviewers
    """

    class InterviewerLevel(models.IntegerChoices):
        """ Model class to give level-options for interviewers """
        LOW = 1, 'HR'
        NORMAL = 2, 'Software Developer'
        HARD = 3, 'Senior Software Developer'
        BOSS = 4, 'Boss'

    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=100, null=True, blank=True)
    intellect = models.IntegerField(default=1, null=False, blank=False)
    coldness = models.IntegerField(default=1, null=False, blank=False)
    coding = models.IntegerField(default=1, null=False, blank=False)
    impress_lvl = models.IntegerField(default=1, null=False, blank=False)
    image = models.ImageField(null=False, blank=False)
    paid = models.BooleanField(default=False)
    level = models.IntegerField(default=InterviewerLevel.LOW, choices=InterviewerLevel.choices)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class Item(models.Model):
    """
    Model for the items
    """

    name = models.CharField(max_length=100, null=False, blank=False)
    price = models.IntegerField(default=0, null=False, blank=False)
    intellect = models.IntegerField(default=0)
    charm = models.IntegerField(default=0)
    coding = models.IntegerField(default=0)
    energy = models.IntegerField(default=0)
    endurance = models.IntegerField(default=0)
    intellect_penalty = models.IntegerField(default=0)
    charm_penalty = models.IntegerField(default=0)
    coding_penalty = models.IntegerField(default=0)
    energy_penalty = models.IntegerField(default=0)
    endurance_penalty = models.IntegerField(default=0)
    permanent = models.BooleanField(default=False)
    image = models.ImageField(null=False, blank=False)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'
