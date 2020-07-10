import pandas as pd
from IPython.display import display, HTML
from constants import user_interface as ui_constants


class QuestEntry:
    """
    A QuestEntry objects contains data used by QuestManager to show information to the player.

    :param name: string that contains the name of the quest
    :param description: string that contains a brief description of the quest
    :param danger_level: int from 1 to 10, represent the risk factor of the quest
    """

    def __init__(self, name, description, danger_level):
        self.name = name
        self.description = description
        self.danger_level = danger_level

    def to_list(self):
        return [self.name, self.description, self.danger_level]


class QuestManager:
    """
    A QuestManager object allow the player to manage sets of QuestEntry objects.

    :param ongoing_quests: list of QuestEntry objects, sets the initial ongoing quests.
    :param completed_quests: list of QuestEntry objects, sets the initial completed quests.
    :param forsaken_quests: list of QuestEntry objects, sets the initial forsaken quests.
    """

    def __init__(self, ongoing_quests=[], completed_quests=[], forsaken_quests=[]):
        self.ongoing_quests = ongoing_quests
        self.forsaken_quests = forsaken_quests
        self.completed_quests = completed_quests
        # do not cut long strings
        pd.set_option('display.max_colwidth', None)

    def add_quest(self, name, description, danger_level=1):
        new_entry = QuestEntry(name, description, danger_level)

        self.ongoing_quests.append(new_entry)

    def remove_quest(self, quest_index):
        self.ongoing_quests.remove(quest_index)

    def forsake_quest(self, quest_index):
        forsaken_quest = self.ongoing_quests[quest_index]
        self.forsaken_quests.append(forsaken_quest)

        self.ongoing_quests.remove(quest_index)

    def complete_quest(self, quest_index):
        completed_quest = self.ongoing_quests[quest_index]
        self.completed_quests.append(completed_quest)

        self.ongoing_quests.remove(quest_index)

    def show_quests(self):
        """
        Print non-empty tables of quests using html snippets.

        TODO: - refactor to avoid code duplication
              - maybe refactor to avoid usage of pandas (use pure HTML)
        """
        ongoing_quests = [quest.to_list() for quest in self.ongoing_quests]
        html_table = pd.DataFrame(ongoing_quests, columns=ui_constants.QUEST_COLUMN_LAYOUT).to_html()

        if ongoing_quests:
            display(HTML(heading(ui_constants.ONGOING_QUESTS) + html_table))

        completed_quests = [quest.to_list() for quest in self.completed_quests]
        html_table = pd.DataFrame(completed_quests, columns=ui_constants.QUEST_COLUMN_LAYOUT).to_html()

        if completed_quests:
            display(HTML(heading(ui_constants.COMPLETED_QUESTS) + html_table))

        forsaken_quests = [quest.to_list() for quest in self.forsaken_quests]
        html_table = pd.DataFrame(forsaken_quests, columns=ui_constants.QUEST_COLUMN_LAYOUT).to_html()

        if forsaken_quests:
            display(HTML(heading(ui_constants.FORSAKEN_QUESTS) + html_table))


# helpers
def heading(string):
    return "<h3>" + string + "</h3>"
