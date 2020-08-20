from dice import dice_roller
from quest import quest_manager
from card import deck
from table import roll_tables
from character import swade_character

from constants import game as game_constants
from constants import assets as assets_constants

from IPython.display import display, HTML


class GameManager:
    def __init__(self):
        self.dice_roller = dice_roller.DiceRoller(game_constants.RANDOM_SEED)
        self.quest_manager = quest_manager.QuestManager()

        # cards
        self.french_deck = self.build_french_deck()

        self.gma_aos_deck = build_unranked_deck(
            assets_constants.GMA_AGE_OF_SAIL_DECK_NAME,
            assets_constants.GMA_AGE_OF_SAIL_DECK_SIZE,
            assets_constants.GMA_AGE_OF_SAIL_DECK_PATH,
            assets_constants.GMA_AGE_OF_SAIL_FILENAME,
            assets_constants.GMA_AGE_OF_SAIL_EXTENSION)

        self.gma_base_deck = build_unranked_deck(
            assets_constants.GMA_BASE_DECK_NAME,
            assets_constants.GMA_BASE_DECK_SIZE,
            assets_constants.GMA_BASE_DECK_PATH,
            assets_constants.GMA_BASE_FILENAME,
            assets_constants.GMA_BASE_EXTENSION)

        self.gma_fantasy_deck = build_unranked_deck(
            assets_constants.GMA_FANTASY_DECK_NAME,
            assets_constants.GMA_FANTASY_DECK_SIZE,
            assets_constants.GMA_FANTASY_DECK_PATH,
            assets_constants.GMA_FANTASY_FILENAME,
            assets_constants.GMA_FANTASY_EXTENSION)

        # tables
        self.tables = self.build_tables()

        # characters
        self.character = self.build_character()

        # CSS styles
        self.set_styles()

    @staticmethod
    def build_french_deck():
        # TODO: - add jokers
        suits = {4: "Hearts", 3: "Diamonds", 2: "Clubs", 1: "Spades"}
        ranks = {14: "Ace", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven",
                 8: "Eight", 9: "Nine", 10: "Ten", 11: "Jack", 12: "Queen", 13: "King"}

        pictures = []
        for suit in suits.values():
            for rank in ranks.values():
                pictures.append("{0}/{1}_of_{2}.png".format(assets_constants.FRENCH_DECK_PATH,
                                                            rank.lower(), suit.lower()))

        return deck.Deck(suits, ranks, pictures)

    @staticmethod
    def set_styles():
        style = "<style>"
        for css_file in assets_constants.STYLES:
            with open(css_file, "r") as css:
                style += ''.join(css.readlines())

        display(HTML(style))

    def build_tables(self):
        tables = []
        for table_file in assets_constants.TABLES:
            tables.append(roll_tables.RollTable().load_from_file(table_file, self.dice_roller))

        return tables

    @staticmethod
    def build_character():
        """
        TODO: - remove this method
        :return:
        """
        character_picture_path = "{0}/assets/player_character/character_picture.jpg".format(assets_constants.ROOT_PATH)

        skill_list = [('Climbing', 'd6'), ('Driving', 'd6'), ('Fighting', 'd12'),
                      ('Gambling', 'd8'), ('Guts', 'd8'), ('Healing', 'd4'),
                      ('Intimidation', 'd6'), ('Investigation', 'd6'), ('Notice', 'd8'),
                      ('Persuasion', 'd6'), ('Piloting', 'd10'), ('Repair', 'd6'),
                      ('Shooting', 'd10'), ('Stealth', 'd8'), ('Streetwise', 'd8'),
                      ('Swimming', 'd6'), ('Taunt', 'd10'), ('Throwing', 'd6'), ('Tracking', 'd6')]

        edges = [('Charismatic',
                  '''
                   Your hero is likable for some reason. She  may be trustworthy or kind, or might just  exude confidence and goodwill.
                   You may Reroll immediately  after failing a Persuasion roll  that’s not a Critical Failure'''),
                 ('Quick',
                  '''
                  Quick characters have lightning-fast reflexes  and a cool head.
                  Whenever you are dealt an  Action Card of Five or lower, you may  discard it and draw again until you  get a card higher than Five.
                  Characters with both the Level  Headed and Quick Edge
                  '''),
                 ('Sweep',
                  '''
                  Sweep allows a character to make a single  Fighting attack and apply it against all targets  in his weapon’s Reach at a -2 penalty (friends  and foes alike).
                  Resolve damage separately  for each enemy that’s hit.  A fighter may only perform a Sweep on
                  ''')]

        hindrances = [('Poverty',
                       '''
                       Half starting funds and the character is always broke.
                       '''),
                      ('Death Wish',
                       '''
                       The hero wants to die after or while completing some epic task.
                       ''')]

        concept = ('Spike is a former member of the criminal Red Dragon Syndicate, '
                   'who left by faking his death after falling in love with a woman called Julia. \n\n'
                   'He is first introduced as the partner of Jet Black, captain of the spaceship '
                   'Bebop: the two are legalized bounty hunters pursuing criminals across the '
                   'populated planets and moons of the solar system.\n\n During his adventures on '
                   'board the Bebop, he is drawn back into a bitter feud with Vicious, '
                   'a rival from the Syndicate who seeks to kill him.')

        character = swade_character.SwadeCharacter(
            name="Spike Spiegel",
            race="Human",
            concept=concept,
            strength="d6",
            agility="d10",
            vigor="d8",
            spirit="d8",
            smarts="d6",
            pace=8,
            parry=10,
            toughness=6,
            armor=2,
            skill_list=skill_list,
            edges=edges,
            hindrances=hindrances,
            picture_path=character_picture_path,
            wounds=2
        )

        return character


def build_unranked_deck(deck_name, deck_size, deck_pictures_path,
                        deck_pictures_filename, deck_pictures_extension):
    suits = {1: "{0}".format(deck_name)}
    ranks = {}

    # TODO: - There is probably a better way to do this
    for i in range(1, deck_size):
        ranks[i] = "{0} GMA card".format(i)

    pictures = []
    for suit in suits.values():
        for rank in ranks.keys():
            pictures.append("{0}/{1}{2}{3}".format(deck_pictures_path, deck_pictures_filename,
                                                   rank, deck_pictures_extension))

    return deck.Deck(suits, ranks, pictures)
