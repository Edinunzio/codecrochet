from abc import ABCMeta, abstractmethod


class Stitch(object):
    """A stitch in a crochet pattern. Stitches have the following properties:

        name: Represents the type of crochet stitch (sl, sc, dc)
        stitch_count: Represents the number of stitches to perform
    """

    __metaclass__ = ABCMeta

    def __init__(self, name=''):
        self.name = name

    @abstractmethod
    def stitching(self, stitch_count):
        """As luck would have it, "stitch" is a noun and verb, anyhow
            returns abstracted python translation of crochet stitches
        """
        pass


class SlipStitch(Stitch):
    """Slip stitch abstraction inheriting from Stitch Abstract Base Class
    """

    def stitching(self, stitch_count):
        """Returns number of slip stitches in pattern
        """
        stitches = [['sl' * stitch_count] for i in range(stitch_count)]
        return stitches


class ChainStitch(Stitch):
    """Chain stitch abstraction inheriting from Stitch Abstract Base Class
    """

    def stitching(self, stitch_count):
        """Returns number of chain stitches in pattern
        """
        stitches = [['ch' * stitch_count] for i in range(stitch_count)]
        return stitches


class SingleCrochet(Stitch):
    """Single crochet abstraction inheriting from Stitch Abstract Base Class
    """

    def stitching(self, stitch_count):
        """Returns number of slip stitches in pattern
        """
        stitches = [['sc' * stitch_count] for i in range(stitch_count)]
        return stitches


class DoubleCrochet(Stitch):
    """Double crochet abstraction inheriting from Stitch Abstract Base Class
    """

    def stitching(self, number_of_stitches):
        """Returns number of slip stitches in pattern
        """
        stitches = [['dc' * stitch_count] for i in range(stitch_count)]
        return stitches
