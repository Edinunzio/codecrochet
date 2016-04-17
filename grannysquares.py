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
