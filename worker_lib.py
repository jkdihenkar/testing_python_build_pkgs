"""
Defining a simple worker that does something
"""


class Worker(object):
    """
    A class that works! Others are lazy :P
    """
    def __init__(self, name):
        self.name = name

    def whoami(self):
        """
        My name is ....
        :return: name of worker
        """
        return self.name

    def do_addition(self, a,b):
        """
        Does simple addition
        :param a: expected numeric value a
        :param b: expected numeric value b
        :return: returns math added values
        """
        self.last_result = a + b
        return self.last_result