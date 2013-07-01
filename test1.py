"""This is a simple program."""


def self_only_no_param(self):
    """Do a thing."""
    print self


def do_thing(self, y):
    """Do a thing."""
    print y


def subtract(k, l=0):
    print k - l


def add(x, y, z):
    """Execute the program.

    Parameters
    ----------
    y: int
        description of y

    """
    print 5 + x


def main(x):
    """Execute the program.

    Parameters
    ----------
    x: type
        description

    """
    print 5 + x

main(3)
