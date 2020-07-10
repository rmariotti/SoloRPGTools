from IPython.display import display, HTML
from constants import tables as table_constants
from constants import user_interface as ui_constants


class RollTable:
    """
    A RollTable object allows the user to get a random result from the table.

    TODO: - refactor this class
          - implement csv import
    :param name: string name of the table.
    :param table: dictionary the keys have to be range of values with no overlap
    :param dice_expression: string the dice expression that the DiceRoller will parse to roll a valid value.
    """

    def __init__(self, name=None, table=None, dice_expression=None, dice_roller=None):
        self.name = name
        self.table = table
        self.dice_expression = dice_expression
        self.dice_roller = dice_roller

    def load_from_file(self, path_to_table, dice_roller):
        """
        Load the content of a RollTable object from form a .table file.

        :param path_to_table: string path to the table file.
        :param dice_roller: DiceRoller object used to generate random values.
        :return: RollTable pointer to an instance of this object.
        TODO: - discard empty lines in table files
              - remove fluent style return self
        """
        self.dice_roller = dice_roller

        with open(path_to_table, 'r') as table_data:
            lines = table_data.readlines()
            # read table header and set name and dice_expression
            self.name = lines[table_constants.TABLE_NAME_LINE_NUMBER]
            self.dice_expression = lines[table_constants.TABLE_DICE_EXPRESSION_LINE_NUMBER]

            # detach header from table body
            lines = [line for line in lines if line not in {self.name, self.dice_expression}]

            self.table = {}

            for line in lines:
                range_str, outcome = line.split(table_constants.DATA_SEPARATOR_CHAR)

                if table_constants.RANGE_SEPARATOR_CHAR in range_str:
                    # in this case the table associate a range of vales to an outcome
                    # es. 1-10 -> outcome
                    range_start, range_end = [int(value)
                                              for value in range_str.split(table_constants.RANGE_SEPARATOR_CHAR)]
                else:
                    # in this case the table associate a single value to an outcome
                    # es. 1 -> outcome
                    range_start = range_end = int(range_str)

                # the range superior limit needs an offset of 1
                range_end = range_end + 1

                self.table[range(range_start, range_end)] = outcome.strip()

        # TODO: - this probably shouldn't return self (non pythonic)
        return self

    def roll(self):
        # roll the dice
        rolled_value = self.dice_roller._roll_expression(self.dice_expression)[0]

        # compare the dice with ranges in the table
        # and get a the corresponding result
        for value_range, outcome in self.table.items():
            if rolled_value in value_range:
                return outcome

        raise ValueError

    def to_html(self):
        """
        Generate an html representation of the table, use "roll_table" CSS class
        to style the tables.

        :returns: string html representations of the object.
        """
        MIN = 0
        MAX = -1

        # generate an HTML representation of the table
        html_table = '<table class="roll_table">'

        # table heading
        html_table += "<tr><th>{0}</th>".format(ui_constants.ROLL)
        html_table += "<th>{0}</th></tr>".format(ui_constants.OUTCOME)

        for roll, outcome in self.table.items():
            html_table += "<tr>"

            range_min = roll[MIN]
            range_max = roll[MAX]

            if range_min == range_max:
                html_table += "<th>{0}</th>".format(range_min)
            else:
                html_table += "<th>{0}-{1}</th>".format(range_min, range_max)

            html_table += "<td>{0}</td>".format(outcome)
            html_table += "</tr>"

        html_table += "</table>"

        return html_table

    def show(self):
        display(HTML(self.to_html()))
