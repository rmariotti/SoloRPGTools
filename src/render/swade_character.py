from IPython.display import display, HTML
from constants import user_interface as ui_constants
from base64 import b64encode

def print(character):
    """
    Render the given SwadeCharacter object on a Jupyter Notebook.

    TODO: - use make template engine instead of hardcoded html snippets.
    :param character: SwadeCharacter character sheet to print.
    """
    character_image = build_character_image(character)
    character_data = build_character_data(character)
    character_concept = build_concept(character)

    basic_info = build_htable([character_image, character_data, character_concept], "basic_info")

    ability_scores = build_ability_score(character)
    skills = build_skills(character)

    traits = build_htable([ability_scores, skills], "traits")

    edges = build_edges(character)
    hindrances = build_character_hindrances(character)

    edges_hindrances = build_htable([edges, hindrances], "edges_hindrances")

    master = build_vtable([basic_info, traits, edges_hindrances])

    display(HTML(master))

def build_character_image(character):
    # TODO: use a placeholder if picture is not found
    return build_image(character.picture_path, "character_pic_container")


def build_character_data(character):
    # init table
    character_data_table = '<table class="character_data">'

    character_data_table += build_row(ui_constants.FIELD_NAME, character.name)
    character_data_table += build_row(ui_constants.FIELD_RACE, character.race)
    character_data_table += build_icon_tracker(ui_constants.FIELD_WOUNDS, ui_constants.ICON_WOUND, character.wounds)
    character_data_table += build_icon_tracker(ui_constants.FIELD_BENNIES, ui_constants.ICON_BENNY, character.bennies)
    character_data_table += build_row(ui_constants.FIELD_PACE, character.pace)
    character_data_table += build_row(ui_constants.FIELD_PARRY, character.parry)
    character_data_table += build_row(ui_constants.FIELD_TOUGHNESS, character.toughness)

    # close table
    character_data_table += '</table>'

    return character_data_table

def build_concept(character):
    # init table
    concept_table = '<table class="concept">'
    concept_table += build_col(ui_constants.FIELD_CONCEPT, character.concept)
    concept_table += '</table>'

    return concept_table

def build_ability_score(character):
    # init table
    ability_score_table = '<table class="ability_score">'

    ability_score_table += build_row(ui_constants.FIELD_STRENGTH, character.strength)
    ability_score_table += build_row(ui_constants.FIELD_AGILITY, character.agility)
    ability_score_table += build_row(ui_constants.FIELD_VIGOR, character.vigor)
    ability_score_table += build_row(ui_constants.FIELD_SPIRIT, character.spirit)
    ability_score_table += build_row(ui_constants.FIELD_SMARTS, character.smarts)

    # close table
    ability_score_table += '</table>'

    return ability_score_table

def build_skills(character):
    skills_table = '<table class="skills"><tr>'

    skills_slices = [character.skill_list[i:i + ui_constants.MAX_ROW_PER_COL]
                    for i in range(0, len(character.skill_list), ui_constants.MAX_ROW_PER_COL)]

    for skills_slice in skills_slices:
        skills_subtable = '<table>'

        for skill in skills_slice:
            skills_subtable += build_row(skill[0], skill[1])

        skills_subtable += '</table>'

        skills_table += '<td>{0}</td>'.format(skills_subtable)

    skills_table += '</tr></table>'

    return skills_table

def build_edges(character):
    # init table
    edges_table = '<table class="edges">'

    for edge in character.edges:
        edges_table += build_col(edge[0], edge[1])

    # close table
    edges_table += '</table>'

    return edges_table

def build_character_hindrances(character):
    # init table
    hindrances_table = '<table class="hindrances">'

    for hindrance in character.hindrances:
        hindrances_table += build_col(hindrance[0], hindrance[1])

    # close table
    hindrances_table += '</table>'

    return hindrances_table

# TODO: - find a better name for those functions
def build_row(ui_field, content):
    return '<tr><th>{0}</th><td>{1}</td></tr>'.format(ui_field, content)

def build_col(ui_field, content):
    return '<tr><th colspan="2">{0}</th></tr><tr><td colspan="2">{1}</td></tr>'.format(ui_field, content)

def build_htable(cells_content_list, css_classes=""):
    table = '<table class="{0}"><tr>'.format(css_classes)
    for cell in cells_content_list:
        table += '<td>{0}</td>'.format(cell)
    table += '</tr></table>'

    return table

def build_vtable(cells_content_list, css_classes=""):
    table = '<table class="{0}">'.format(css_classes)
    for cell in cells_content_list:
        table += '<tr><td>{0}</tr></td>'.format(cell)
    table += '</table'

    return table

def embed_image(content):
    return '<img src="data:image/png;base64,{0}">'.format(content)

def build_image(image_path, css_container_classes=""):
    # read image file
    file = open(image_path, 'rb')
    image = file.read()

    image_encoded = b64encode(image).decode('ascii')

    image_container = '<div class="{0}">'.format(css_container_classes)
    image_container += embed_image(image_encoded)
    image_container += '</div>'

    file.close()

    return image_container

def build_icon_tracker(ui_field, ui_icon, icon_number):
    icons = ""
    for i in range(icon_number):
        icons += build_image(ui_icon, "tracker_icons")

    return build_row(ui_field, icons)
