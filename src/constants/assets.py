from pathlib import Path

ROOT_PATH = Path(__file__).parent.parent

ASSETS_PATH = "{0}/assets".format(ROOT_PATH)
CARD_PICTURE_PATH = "{0}/cards".format(ASSETS_PATH)
TABLES_PATH = "{0}/tables".format(ASSETS_PATH)
STYLES_PATH = "{0}/styles".format(ASSETS_PATH)
TEMPLATES_PATH = "{0}/templates".format(ASSETS_PATH)

TABLE_FILES = ["event_focus.table",
               "event_meaning_action.table",
               "event_meaning_subject.table"]

# TODO: - load config from file
STYLES = ["{0}/character_sheet.css".format(STYLES_PATH)]
TABLES = ["{0}/{1}".format(TABLES_PATH, table_file) for table_file in TABLE_FILES]

D20_CHAR_TEMPLATE = "{0}/d20_character_sheet.html".format(TEMPLATES_PATH)
