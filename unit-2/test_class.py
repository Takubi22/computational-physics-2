# a test class is useful to hold data that we might want setup
# for every test.

import numpy as np
from numpy.testing import assert_array_equal

class TestClassExample(object):

    @classmethod
    def setup_class(cls):
        """ this is run once for each class, before any tests """
        print("Startint tests.")
        pass

    @classmethod
    def teardown_class(cls):
        """ this is run once for each class, after all tests """
        print("CLeaning up.")
        pass

    def setup_method(self):
        """ this is run before each of the test methods """
        self.a = np.arange(48).reshape(8, 6)

    def teardown_method(self):
        """ this is run after each of the test methods """
        pass

    def test_max(self):
        assert self.a.max() == 24

    def test_flat(self):
        assert_array_equal(self.a.flat, np.arange(24))
