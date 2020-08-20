from pathlib import Path

ROOT_PATH = Path(__file__).parent.parent

ASSETS_PATH = "{0}/assets".format(ROOT_PATH)

# cards and decks
CARD_PICTURE_PATH = "{0}/cards".format(ASSETS_PATH)

FRENCH_DECK_PATH = "{0}/french_deck".format(CARD_PICTURE_PATH)

GMA_BASE_DECK_NAME = "GMA Base"
GMA_BASE_DECK_SIZE = 120
GMA_BASE_DECK_PATH = "{0}/gma_base".format(CARD_PICTURE_PATH)
GMA_BASE_FILENAME = "GMA Base VTT_Part"
GMA_BASE_EXTENSION = ".jpg"

GMA_AGE_OF_SAIL_DECK_NAME = "GMA Age of Sail"
GMA_AGE_OF_SAIL_DECK_SIZE = 120
GMA_AGE_OF_SAIL_DECK_PATH = "{0}/gma_age_of_sail".format(CARD_PICTURE_PATH)
GMA_AGE_OF_SAIL_FILENAME = "GMA Age of Sail VTT_Part"
GMA_AGE_OF_SAIL_EXTENSION = ".jpg"

GMA_FANTASY_DECK_NAME = "GMA Fantasy"
GMA_FANTASY_DECK_SIZE = 120
GMA_FANTASY_DECK_PATH = "{0}/gma_fantasy".format(CARD_PICTURE_PATH)
GMA_FANTASY_FILENAME = "GMA Fantasy VTT_Part"
GMA_FANTASY_EXTENSION = ".jpg"

# tables and generators
TABLES_PATH = "{0}/tables".format(ASSETS_PATH)
TABLE_FILES = [
    "event_focus.table",
    "event_meaning_action.table",
    "event_meaning_subject.table"
    ]
TABLES = ["{0}/{1}".format(TABLES_PATH, table_file) for table_file in TABLE_FILES]

# css styles
STYLES_PATH = "{0}/styles".format(ASSETS_PATH)

# html templates
TEMPLATES_PATH = "{0}/templates".format(ASSETS_PATH)
D20_CHAR_TEMPLATE = "{0}/d20_character_sheet.mako".format(TEMPLATES_PATH)

# TODO: - load config from file
STYLES = ["{0}/character_sheet.css".format(STYLES_PATH)]
