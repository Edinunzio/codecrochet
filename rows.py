import itertools
#Abstracting Row of crochet stitches


class Row(object):

    def __init__(self, row_index, list_of_stitches):
        self.row_index = row_index
        self.list_of_stitches = list_of_stitches

    def get_spaces():
        """Abstracted helper function.
        This function only serves to get the sticheable spaces in the row.
        I am treating a standard round/row in crochet as a list in python.
        Each stitch is represented as an item in the list.
        """

        #Flattening any nested lists passed as stitches
        stitch_list = itertools.chain(*list_of_stitches)
        spaces = len(stitch_list)
        return spaces
