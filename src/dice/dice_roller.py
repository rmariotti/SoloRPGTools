import random


class DiceRoller:
    """
    A DiceRoller object allows to get seeded random values that remains the same across different runs.

    TODO: replace indexes (1 and 0) with constants
    :param seed: integer is the seed of the random numbers.
    """

    def __init__(self, seed):
        random.seed(seed)

    def _roll_expression(self, dice_expression, exploding=False):
        """
        Parse dice expressions containing sums, subtractions and constants then rolls the dice.
        """
        # the expression is split at every + symbol
        # dice_list_sum contains the slices of the split
        # once those slices are parsed they'll be summed
        dice_list_sum = dice_expression.split('+')

        # the strings in dice_list_sum are split once more (this time at every - symbol)
        # dice_list_sum now contains lists of strings that needs to be parsed an then subtracted
        dice_list_sum = [expression.split('-') for expression in dice_list_sum]

        # dice_list_sum = [A, B, ..., N] where A, B, ..., N are expressions that
        # once parsed needs to be summed (result = A + B + ... + N)
        # with A = [R, S, ..., Z] where R, S, ..., Z are expressions that once
        # parsed needs to be subtracted (A = R - S - ... - Z)
        # R, S, ..., Z are either constants or expressions in the format "XdY"
        total_roll = 0
        roll_log = []
        for dice_list_sub in dice_list_sum:
            first = True  # needed to keep track of the first element
            for constant_or_xdy in dice_list_sub:
                roll = self._parse_constant_roll_dice(constant_or_xdy, exploding)

                roll_log.extend(roll[1])

                # non first element are always negative
                if not first:
                    total_roll -= roll[0]

                # the first elemen is always positive
                else:
                    first = False
                    total_roll += roll[0]

        # remove all occurrences of None in the log
        roll_log = [element for element in roll_log if element != []]

        return total_roll, roll_log

    def _parse_constant_roll_dice(self, dice_expression, exploding=False):
        """
        Parse input in format "XdY" or "K", in the first case rolls the dice.

        TODO: refactor this docstring
        """
        # if the string contains 'd' needs to be parsed and rolled
        if 'd' in dice_expression:
            return self._roll_dice(dice_expression, exploding)
        # else it is a constants, no need to roll
        else:
            return (int(dice_expression), [])

    def _roll_dice(self, dice_expression, exploding=False):
        """
        Parse expressions in the format "XdY" and rolls the dice.

        :param dice_expression: string of dice expression XdY, a Y-sided die is rolled X-times.
        :param exploding: boolean if true every die that gets the maximum possible value are
                          rerolled and added to the total.
        :return: tuple containing and integer of the sum of the numbers rolled and a list
                 with the results of each die rolled.
        """
        # parse expression
        (dice_number, dice_type) = [int(num) for num in dice_expression.split('d')]

        total_roll = 0
        roll_log = []
        # for each dice to roll
        for i in range(dice_number):
            # roll a dice_type-sided die
            rolled_number = random.randint(1, dice_type)
            roll_log.append(rolled_number)
            total_roll += rolled_number

            while exploding and rolled_number == dice_type:
                rolled_number = random.randint(1, dice_type)
                roll_log.append(rolled_number)
                total_roll += rolled_number

        return total_roll, roll_log
