from collections import namedtuple


class D20Character:
    def __init__(self, name, level, ability_scores, defence_scores, hp,
                 recovery_dice, class_name, race_name, out, icon_relationships,
                 backgrounds, picture_path, class_talents, class_features, racial_power):
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


class AbilityScores:
    """
    TODO: - re-implement iterator
    """
    def __init__(self, strength, dexterity, constitution, intellect, wisdom, charisma):
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


class AbilityScore:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def get_modifier(self):
        return (self.value - 10) // 2

'''
class Power:
    """
    TODO: - use namedtuple (?)
    :param name: string power's name
    :param description: string power's description
    :param feats: tuple of tuples in the format ((string feat name, string feat description) ... )
    """
    def __init__(self, name, description, feats=()):
        self.name = name
        self.description = description
        self.feats = feats
'''


Background = namedtuple('Background', ['name', 'value'])
Power = namedtuple('Power', ['name', 'description', 'feats'])
Feat = namedtuple('Feat', ['type', 'description'])
IconRelationship = namedtuple('IconRelationship', ['name', 'type'])