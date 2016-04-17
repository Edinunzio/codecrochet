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
