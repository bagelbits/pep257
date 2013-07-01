"""This is a simple program."""


def request_only_param(request):
    """Do a thing."""
    print 5


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
