from collections import namedtuple
import csv


class AbilityScores:
    """
    TODO: - re-implement iterator
    """
    def __init__(self, strength=None, dexterity=None, constitution=None,
                 intellect=None, wisdom=None, charisma=None):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intellect = intellect
        self.wisdom = wisdom
        self.charisma = charisma

        self._ability_scores = (strength, dexterity, constitution, intellect, wisdom, charisma)
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._ability_scores):
            value = self._ability_scores[self._index]
            self._index += 1
            return value
        else:
            self._index = 0
            raise StopIteration

class D20Character:
    def __init__(self, name=None, level=1, ability_scores=AbilityScores(),
                 defence_scores=(10, 10, 10), hp=0, recovery_dice=None,
                 class_name=None, race_name=None, out=None, icon_relationships=[],
                 backgrounds=[], picture_path=None, class_talents=[], class_features=[],
                 racial_power=None, powers_and_spells=[]):
        """
        TODO: - document class
        :param name: string
        :param level: integer
        :param ability_scores: AbilityScores
        :param defence_scores: tuple of integers
        :param hp: integer
        :param recovery_dice: string
        :param class_name: string
        :param race_name: string
        :param out: string
        :param icon_relationships: list
        :param backgrounds:
        :param picture_path:
        :param class_talents:
        :param class_features:
        :param racial_power:
        :param powers_and_spells:
        """
        self.name = name
        self.level = level
        self.ability_scores = ability_scores
        self.ac, self.pd, self.md = defence_scores
        self.hp = self.hp_max = hp
        self.recoveries, self.recovery_die = recovery_dice
        self.recoveries_max = self.recoveries

        self.class_name = class_name
        self.race_name = race_name
        self.out = out
        self.icon_relationships = icon_relationships
        self.backgrounds = backgrounds

        self.picture_path = picture_path

        self.class_talents = class_talents
        self.class_features = class_features
        self.racial_power = racial_power
        self.powers_and_spells = powers_and_spells

    def from_csv(self, csv_path):
        """
        TODO: - is there a way to avoid this long if-else statement?

        :param csv_path: path to the csv containing character's data
        """
        with open(csv_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter='\t')

            for row in csv_reader:
                # Character basic info
                if row[0] == "Name":
                    self.name = row[1]

                elif row[0] == "Race":
                    self.race_name = row[1]

                elif row[0] == "Class":
                    self.class_name = row[1]

                elif row[0] == "Level":
                    self.level = int(row[1])

                # Ability Scores
                elif row[0] == "Str":
                    self.ability_scores.strength = AbilityScore("Str", row[1])

                elif row[0] == "Dex":
                    self.ability_scores.dexterity = AbilityScore("Dex", row[1])

                elif row[0] == "Con":
                    self.ability_scores.constitution = AbilityScore("Con", row[1])

                elif row[0] == "Int":
                    self.ability_scores.intellect = AbilityScore("Int", row[1])

                elif row[0] == "Wis":
                    self.ability_scores.wisdom = AbilityScore("Wis", row[1])

                elif row[0] == "Cha":
                    self.ability_scores.charisma = AbilityScore("Cha", row[1])

                # Additional character stats
                elif row[0] == "AC":
                    self.ac = int(row[1])

                elif row[0] == "MD":
                    self.md = int(row[1])

                elif row[0] == "PD":
                    self.pd = int(row[1])

                elif row[0] == "HP":
                    self.hp_max = self.hp = int(row[1])

                elif row[0] == "Recoveries":
                    self.recoveries = self.recoveries_max = int(row[1])

                elif row[0] == "Recovery Dice":
                    self.recovery_die = row[1]

                # Backgrounds
                elif row[0] == "Background":
                    self.backgrounds.append(Background(row[1], row[2]))

                # Icon Relationships
                elif row[0] == "Icon Relationship":
                    self.icon_relationships.append(IconRelationship(row[1], row[2]))

                # OUT
                elif row[0] == "OUT":
                    self.out = row[1]

        return None


class AbilityScore:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def get_modifier(self):
        return (self.value - 10) // 2


Background = namedtuple('Background', ['name', 'value'])
Background.__doc__ = """
:param name: string background's name (ex. warrior, wizard)
:param value: int numeric value of the bonus on skill checks
"""


Power = namedtuple('Power', ['name', 'description', 'feats'])
Power.__doc__ = """
:param name: string power's name
:param description: string power's description
:param feats: tuple of Feat objects
"""


Feat = namedtuple('Feat', ['type', 'description'])
Feat.__doc__ = """
:param type: string type of feat (ex. adventurer feat, champion feat ...) 
:param description: string text describing feat's effects
"""


IconRelationship = namedtuple('IconRelationship', ['name', 'type'])
IconRelationship.__doc__ = """
:param name: string name of the icon
:param type: string relationship's type (positive, negative, conflicted)
"""