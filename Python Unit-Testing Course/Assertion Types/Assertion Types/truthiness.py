import unittest


class TestIntegerTruthiness(unittest.TestCase):
    def test_zero(self):
        """check that the thruthiness of the integer zero is False"""
        self.assertTrue(bool(0) == False)

    def test_one(self):
        """check that the thruthiness of the integer one is True"""
        self.assertTrue(bool(1) == True)

    def test_other_value(self):
        """check the thruthiness of an integer other than zero"""
        self.assertTrue(bool(2) == True)


class TestNoneTruthiness(unittest.TestCase):
    def test_none(self):
        """check the thruthiness of None"""
        self.assertFalse(None)


class TestContainerTruthiness(unittest.TestCase):
    # Note:
    # -----
    # Methods whose name starts with "_test" are not considered test methods,
    # just like all methods whose name doesn't begin with "test".

    def _test_container_class(self, empty_container, non_empty_container):
        self.assertFalse(empty_container)
        self.assertTrue(non_empty_container)

    def test_list(self):
        _test_container_class(self,[],[1,2,3])

    def test_tuple(self):
        _test_container_class(self, (), (1, 2, 3))

    def test_set(self):
        implement this test using _test_container_class()

    def test_dict(self):
        implement this test using _test_container_class()
