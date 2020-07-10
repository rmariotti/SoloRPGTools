import random
from matplotlib.pyplot import figure, imshow, axis
from matplotlib.image import imread


class Deck:
    """
    A Deck object allows the player to interact with a deck of cards.

    :param suits: dictionary
    :param ranks: dictionary
    """

    def __init__(self, suits, ranks, pictures=None):
        self.cards = [Card(suit, suit_str, rank, rank_str)
                      for suit, suit_str in suits.items()
                      for rank, rank_str in ranks.items()]

        if pictures is not None:
            for card, picture in zip(self.cards, pictures):
                card.picture = picture

        self.drawn_cards = []

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self, card_number=1):
        """
        Draw one or more card from the deck.

        :param card_number: integer number of cards to draw.
        :return: list of drawn cards.
        """
        drawn = []
        for i in range(card_number):
            drawn.append(self.cards.pop())

        self.drawn_cards.extend(drawn)

        return drawn

    def reinsert_drawn(self):
        self.cards.extend(self.drawn_cards)
        self.drawn_cards = []

    def sort(self):
        self.cards.sort()

    def reset_deck(self):
        self.reinsert_drawn()
        self.sort()


class Card:
    """
    A Card object represent a playing card of deck.

    :param suit: int describes card's suit.
    :param suit_str: string card's suit in letter.
    :param rank: integer describes card's rank.
    :param rank_str: string card's rank in letter.
    :param picture: string path to a picture.
    """

    def __init__(self, suit, suit_str, rank, rank_str, picture=None):
        self.suit = suit
        self.suit_str = suit_str
        self.rank = rank
        self.rank_str = rank_str

        self.picture = picture

    def __lt__(self, other):
        if not self.rank == other.rank:
            return self.rank < other.rank
        else:
            return self.suit < other.suit

    def __le__(self, other):
        if not self.rank == other.rank:
            return self.rank < other.rank
        else:
            return self.suit <= other.suit

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def __ne__(self, other):
        return self.rank != other.rank or self.suit != other.suit

    def __gt__(self, other):
        if not self.rank == other.rank:
            return self.rank > other.rank
        else:
            return self.suit > other.suit

    def __ge__(self, other):
        if not self.rank == other.rank:
            return self.rank > other.rank
        else:
            return self.suit >= other.suit

    def __str__(self):
        return "{0} of {1}".format(self.rank_str, self.suit_str)


def show_images_horizontally(list_of_files):
    fig = figure()
    number_of_files = len(list_of_files)

    for i in range(number_of_files):
        a = fig.add_subplot(1, number_of_files, i + 1)
        image = imread(list_of_files[i])
        imshow(image, cmap='Greys_r')
        axis('off')
