ASSETS_PATH = "assets"
CARD_PICTURE_PATH = "{0}/cards".format(ASSETS_PATH)
TABLES_PATH = "{0}/tables".format(ASSETS_PATH)
STYLES_PATH = "{0}/styles".format(ASSETS_PATH)

TABLE_FILES = ["event_focus.table",
               "event_meaning_action.table",
               "event_meaning_subject.table"]

# TODO: - load config from file
STYLES = ["{0}/character_sheet.css".format(STYLES_PATH)]
TABLES = ["{0}/{1}".format(TABLES_PATH, table_file) for table_file in TABLE_FILES]
