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

    @classmethod
    def new_item(cls):
        """
        Method for generating a new weapon.
        Method takes in Paid Status and User Level.
        Level of the weapon is detemined at random,
        along with the rarity of the weapon.
        The base stats of the weapon generated are then
        modified by a random amount, the limits of the
        multiplier are effected by the weapon's current
        level and rarity.
        The stat modifications are applied by a order of
        magnitute equivalent to the weapon's rarity.
        """
        # Obtain new weapon
        weapon = cls.objects.get_random("Weapon", paid, level)

        # Determine level and rarity
        if level > 1:
            weapon.level = randint(1, level)  # nosec
            weapon.rarity = rarity_recursive(weapon.level)
        else:
            weapon.level = 1
            weapon.rarity = 1

        rarity_list = ["Common", "Uncommon", "Rare", "Epic", "Mythic"]
        weapon.rarity_text = rarity_list[weapon.rarity-1]

        # Apply modification in order of magnitude (rarity)
        # Double underscore used in for loop to avoid unused variable
        for __ in range(weapon.rarity):

            # Modify stats based on level and rarity
            weapon.base_hp = stat_modifier(weapon.base_hp,
                                           weapon.level,
                                           weapon.rarity)
            weapon.base_attack = stat_modifier(weapon.base_attack,
                                               weapon.level,
                                               weapon.rarity)
            weapon.base_speed = stat_modifier(weapon.base_speed,
                                              weapon.level,
                                              weapon.rarity)
            weapon.base_defense = stat_modifier(weapon.base_defense,
                                                weapon.level,
                                                weapon.rarity)
        return weapon

    @classmethod
    def new_enemy(cls, paid, level):
        """
        Method for generating a new enemy.
        Method takes in Paid Status and User Level.
        Level of the Enemy is detemined at random.
        The base stats of the enemy generated are modified
        n number of times, where n is the monster's level, based
        on the current monster's level.
        Enemy must be over level 1 for the modification to occur.
        """

        # Obtain new enemy
        enemy = cls.objects.get_random("Enemy", paid, level)
        # Determine level
        if level > 1:
            enemy.level = randint(1, level)  # nosec
            # Modify stats based on level (progressive)
            # Double underscore used in for loop to avoid unused variable
            for __ in range(enemy.level - 1):
                enemy.base_hp = stat_modifier(enemy.base_hp,
                                              enemy.level)
                enemy.base_attack = stat_modifier(enemy.base_attack,
                                                  enemy.level)
                enemy.base_speed = stat_modifier(enemy.base_speed,
                                                 enemy.level)
                enemy.base_defense = stat_modifier(enemy.base_defense,
                                                   enemy.level)
        else:
            enemy.level = 1
        return enemy
