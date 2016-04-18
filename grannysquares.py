# DO NOT WRITE ACTUAL CODE LIKE THIS. THIS IS FOR EXPERIMENTAL PURPOSES


def sl(number_of_stitches):
    """This is an abstraction of a slip stitch.
    For argument's sake, we're assuming all stitch functions will be
    performed outside this scope
    @number_of_stitches is how many times we want to execute "sl"
    within the current space/stitch
    """
    return sl * number_of_stitches


def ch(number_of_stitches):
    """This is an abstraction of a chain stitch.
    For argument's sake, we're assuming all stitch functions will be
    performed outside this scope
    @number_of_stitches is how many times we want to execute "ch"
    within the current space/stitch
    """
    return ch * number_of_stitches


def dc(number_of_stitches):
    """This is an abstraction of a double crochet stitch.
    For argument's sake, we're assuming all stitch functions will be
    performed outside this scope
    @number_of_stitches is how many times we want to execute "dc"
    within the current space/stitch
    """
    return dc * number_of_stitches


def get_spaces(row):
    """Another abstracted function that serves as a "helper".
    This function only serves to get the sticheable spaces in the row.
    I am treating a standard round/row in crochet as a list in python.
    Each stitch is represented as an item in the list.
    This will not work, and is being used as a way to loop through the row
    using the computer and not a human's eyes.
    """
    spaces = ''  # No need to abstract this out for the overall purpose
    return spaces

# Round One:
begin_ring = ch(3)  # Chain 3.
begin_ring[0].dc(1)  # Dc into first chain.
begin_ring[0].dc(1)  # Dc again into first chain.

ch(2)  # Chain 2; this create the space that will become your first corner
begin_ring[0].dc(3)  # 3 dc into the same chain spot.
ch(2)  # Ch 2 to make your next corner

# Below repeats that previous step twice more
begin_ring[0].dc(3)
ch(2)
begin_ring[0].dc(3)
ch(2)

begin_ring[2].sl(1)  # Slip stitch in top chain of "chain three" to close round

# Round Two:
spaces = get_spaces(round_1)
begin_stitch = spaces[0].ch(3)  # To begin next round, you will chain three
# This counts as the first dc of the round.
spaces[0].dc(2)  # Make 2 dc into the same corner as the ch 3.

# In the following corner: 3 dc, 2 ch, 3 dc.
spaces[1].dc(3)
spaces[1].ch(2)
spaces[1].dc(3)  # This makes the new corner.

# Repeating in the next corner.
spaces[2].dc(3)
spaces[2].ch(2)
spaces[2].dc(3)

# In the final corner, you will make 3 dc, chain 2, then slip stitch to the
# top of first chain in the first "chain three" to close the round
spaces[2].dc(3)
spaces[2].ch(2)
begin_stitch[2].sl(1)

# Round Three:
spaces_2 = get_spaces(round_2)
begin_stitch = spaces_2[0].ch(3)  # Chain 3
spaces_2[0].dc(2)  # 2 dc in same corner
spaces_2[1].dc(3)  # 3 dc in non corner space

# Next space is corner
spaces_2[2].dc(3)
spaces_2[2].ch(2)
spaces_2[2].dc(3)

# Repeat around the square
