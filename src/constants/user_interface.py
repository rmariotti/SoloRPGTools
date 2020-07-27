from constants import assets as assets_constants

# character sheet
FIELD_NAME = "Name"
FIELD_RACE = "Race"
FIELD_CONCEPT = "Concept"
FIELD_WOUNDS = "Wounds"
FIELD_BENNIES = "Bennies"
FIELD_PACE = "Pace"
FIELD_PARRY = "Parry"
FIELD_TOUGHNESS = "Toughness"
FIELD_STRENGTH = "Strength"
FIELD_AGILITY = "Agility"
FIELD_VIGOR = "Vigor"
FIELD_SPIRIT = "Spirit"
FIELD_SMARTS = "Smarts"

MAX_ROW_PER_COL = 5

ICON_BENNY = '{0}/icons/benny.png'.format(assets_constants.ASSETS_PATH)
ICON_WOUND = '{0}/icons/wound.png'.format(assets_constants.ASSETS_PATH)

ICON_13THAGE_LOGO = '{0}/icons/13thage_logo.png'.format(assets_constants.ASSETS_PATH)

# quest manager
QUEST_COLUMN_LAYOUT = ["Name", "Description", "Challenge"]

ONGOING_QUESTS = "Ongoing Quests"
COMPLETED_QUESTS = "Completed Quests"
FORSAKEN_QUESTS = "Failed/Forsaken Quests"

# tables user interface
ROLL = 'Roll'
OUTCOME = 'Outcome'