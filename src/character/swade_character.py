from constants import user_interface as ui_constants
from IPython.display import display, HTML


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

    def show(self):
        # TODO: - refactor decouple initialization from assignments
        #       - split this blob in smaller methods
        # style the character sheet tables
        # TODO: - let the game manager handle styles
        # style = "<style>{0}</style>".format(CHARACTER_SHEET_STYLE)
        # master_table = style

        # the master table will have 1 row and n columns, each containing different
        # information on the player character
        master_table = '<table class="character_sheet">'

        basic_info_subtable = '<table class="basic_info">'
        basic_info_subtable += '<tr>'

        # the first column will contain the character picture
        # TODO: - use constants for height and width
        character_picture = '<div class="character_pic_container">'
        character_picture += '<img class="character_pic" src="{0}">'.format(self.picture_path)
        character_picture += '</div>'

        basic_info_subtable += '<td class="character_pic_cell">{0}</td>'.format(character_picture)

        # the second column will contain basic information on the character
        # such as name, race, concept, wounds and bennies
        character_data_subtable = '<table class="character_data">'
        # name row
        character_data_subtable += build_row(ui_constants.FIELD_NAME, self.name)
        # race row
        character_data_subtable += build_row(ui_constants.FIELD_RACE, self.race)
        # TODO: - avoid code duplication bennies/wounds
        # wound row
        wounds = '<div class="tracker_icons">'
        for i in range(self.wounds):
            wounds += insert_image(ui_constants.ICON_WOUND)
        wounds += '</div>'
        character_data_subtable += build_row(ui_constants.FIELD_WOUNDS, wounds)

        # bennies row
        bennies = '<div class="tracker_icons">'
        for i in range(self.bennies):
            bennies += insert_image(ui_constants.ICON_BENNY)
        bennies += '</div>'
        character_data_subtable += build_row(ui_constants.FIELD_BENNIES, bennies)

        character_data_subtable += build_row(ui_constants.FIELD_PACE, self.pace)

        character_data_subtable += build_row(ui_constants.FIELD_PARRY, self.parry)

        character_data_subtable += build_row(ui_constants.FIELD_TOUGHNESS, self.toughness)

        character_data_subtable += '</table>'

        basic_info_subtable += '<td>{0}</td>'.format(character_data_subtable)

        concept_subtable = '<table class="concept">'
        concept_subtable += build_col(ui_constants.FIELD_CONCEPT, self.concept)
        concept_subtable += '</table>'

        basic_info_subtable += '<td>{0}</td>'.format(concept_subtable)

        basic_info_subtable += '</tr>'
        basic_info_subtable += '</table>'

        master_table += '<tr><td>{0}</td></tr>'.format(basic_info_subtable)

        traits_subtable = '<table class="traits">'
        traits_subtable += '<tr>'

        # the third column will contain the character's ability score
        ability_score_table = '<table>'
        # strength row
        ability_score_table += build_row(ui_constants.FIELD_STRENGTH, self.strength)
        # agility row
        ability_score_table += build_row(ui_constants.FIELD_AGILITY, self.agility)
        # vigor row
        ability_score_table += build_row(ui_constants.FIELD_VIGOR, self.vigor)
        # spirit row
        ability_score_table += build_row(ui_constants.FIELD_SPIRIT, self.spirit)
        # smarts row
        ability_score_table += build_row(ui_constants.FIELD_SMARTS, self.smarts)

        ability_score_table += '</table>'
        traits_subtable += '<td>{0}</td>'.format(ability_score_table)

        # the fourth column will contain info about character's skills
        skill_slices = [self.skill_list[i:i + ui_constants.MAX_ROW_PER_COL]
                        for i in range(0, len(self.skill_list), ui_constants.MAX_ROW_PER_COL)]

        for skill_slice in skill_slices:
            skill_subtable = '<table>'

            for skill in skill_slice:
                skill_subtable += build_row(skill[0], skill[1])

            skill_subtable += '</table>'
            traits_subtable += '<td>{0}</td>'.format(skill_subtable)

        traits_subtable += '</tr>'
        traits_subtable += '</table>'

        master_table += '<tr><td>{0}</td></tr>'.format(traits_subtable)

        edges_hindrances_subtable = '<table class="edges_hindrances">'

        edges_subtable = '<table class="edges">'
        for edge in self.edges:
            edges_subtable += build_col(edge[0], edge[1])
        edges_subtable += '</table>'

        edges_hindrances_subtable += '<td>{0}</td>'.format(edges_subtable)

        hindrances_subtable = '<table class="hindrances">'
        for hindrance in self.hindrances:
            hindrances_subtable += build_col(hindrance[0], hindrance[1])
        hindrances_subtable += '</table>'

        edges_hindrances_subtable += '<td>{0}</td>'.format(hindrances_subtable)

        edges_hindrances_subtable += '</table>'

        master_table += '<tr><td>{0}</td></tr>'.format(edges_hindrances_subtable)

        display(HTML(master_table))


# helpers
# TODO: - find a better name for those functions
def build_row(ui_field, content):
    return '<tr><th>{0}</th><td>{1}</td></tr>'.format(ui_field, content)


def build_col(ui_field, content):
    return '<tr><th colspan="2">{0}</th></tr><tr><td colspan="2">{1}</td></tr>'.format(ui_field, content)


def insert_image(image_path):
    return '<img src="{0}">'.format(image_path)
