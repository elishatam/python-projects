import unittest


class TestPossibleResults(unittest.TestCase):
    def test_success(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_failure(self):
        self.assertEqual('foo'.upper(), 'Foo')

    def test_error(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(3)
