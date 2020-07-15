class SwadeCharacter:
    """
    This class represents the player character of a SWADE game.
    TODO: - refactor comments

    :param name: string character's name.
    :param race: string character's race.
    :param concept: string brief character description.
    :param strength: string dice expression for character's strength.
    :param agility: string dice expression for character's agility.
    :param vigor: string dice expression for character's vigor.
    :param smarts: string dice expression for character's smarts.
    :param spirit: string dice expression for character's spirit.
    :param skill_list: list of tuple(string, string) the first element of each tuple
                       is the name of the skill, the second is the associated dice expression.
    """

    def __init__(self, name, race, concept, agility,
                 strength, smarts, spirit, vigor,
                 pace, parry, toughness, armor,
                 skill_list, edges, hindrances,
                 bennies=3, wounds=0, picture_path=None):
        # character info
        self.name = name
        self.race = race
        self.concept = concept
        self.picture_path = picture_path

        # attributes (as in in-game attributes)
        self.strength = strength
        self.agility = agility
        self.vigor = vigor
        self.spirit = spirit
        self.smarts = smarts

        # derived attributes
        self.pace = pace
        self.parry = parry
        self.toughness = toughness
        self.armor = armor

        # game vars
        self.bennies = bennies
        self.wounds = wounds

        self.skill_list = skill_list
        self.edges = edges
        self.hindrances = hindrances