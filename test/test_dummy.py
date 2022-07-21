# Dummy test file while we have no real tests.

import unittest


class Dummy(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDummy(self):
        pass


if __name__ == "__main__":
    unittest.main()
