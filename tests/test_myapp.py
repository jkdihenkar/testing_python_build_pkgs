import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from myapp.worker_lib import Worker


class TestWorkerLib(unittest.TestCase):
    """Testing worker lib class for py36"""
    def setUp(self):
        self.worker = Worker("Addition Worker")

    def test_positive_addition_pp(self):
        self.assertEquals(self.worker.do_addition(7,3), 10)

    def test_positive_addition_pn(self):
        self.assertEquals(self.worker.do_addition(7,-3), 4)

    def test_positive_addition_np(self):
        self.assertEquals(self.worker.do_addition(-7,3), -4)

    def test_positive_assition_nn(self):
        self.worker.do_addition(self.worker.do_addition(-7,-3), -10)

    def test_selfintro(self):
        self.assertEquals(self.worker.whoami(), "Addition Worker")