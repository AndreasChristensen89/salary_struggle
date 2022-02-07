from django.db import models

# not migrated
class Codex(models.Model):
    """
    """

    class Meta:
        verbose_name_plural = 'Codex'

    class TypeChoices(models.TextChoices):
        """Type Text Choices for model Type field"""
        INTERVIEWER = 'Interviewer', _('Interviewer')
        ITEM = 'Item', _('Weapon')

    class InterviewerLevel(models.IntegerChoices):
        LOW = 1, 'HR'
        NORMAL = 2, 'Software Developer'
        HARD = 3, 'Senior Software Developer'
        BOSS = 4, 'Boss'

    name = models.CharField(max_length=100)
    alpha_name = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=15, choices=TypeChoices.choices,
                            default=TypeChoices.INTERVIEWER)
    intellect = models.IntegerField(default=0)
    charm = models.IntegerField(default=0)
    intellect = models.IntegerField(default=0)
    endurance = models.IntegerField(default=0)
    image = models.ImageField(null=False, blank=False)
    paid = models.BooleanField(default=False)
    level = models.IntegerField(default=InterviewerLevel.LOW, choices=InterviewerLevel.choices)

    def __str__(self):
        return self.
