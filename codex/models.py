from django.db import models


class Interviewer(models.Model):
    """
    """

    class InterviewerLevel(models.IntegerChoices):
        LOW = 1, 'HR'
        NORMAL = 2, 'Software Developer'
        HARD = 3, 'Senior Software Developer'
        BOSS = 4, 'Boss'

    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=100, null=True, blank=True)
    intellect = models.IntegerField(default=1)
    coldness = models.IntegerField(default=1)
    coding = models.IntegerField(default=1)
    impress_lvl = models.IntegerField(default=1)
    image = models.ImageField(null=False, blank=False)
    paid = models.BooleanField(default=False)
    level = models.IntegerField(default=InterviewerLevel.LOW, choices=InterviewerLevel.choices)

    def __str__(self):
        return self.friendly_name


class Item(models.Model):
    """
    """

    name = models.CharField(max_length=100, null=False, blank=False)
    price = models.IntegerField(default=0, null=False, blank=False)
    intellect = models.IntegerField(default=0)
    charm = models.IntegerField(default=0)
    coding = models.IntegerField(default=0)
    energy = models.IntegerField(default=0)
    image = models.ImageField(null=False, blank=False)

    def __str__(self):
        return self.name
