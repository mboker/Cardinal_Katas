import unittest
from kata_one import *

class Tests(unittest.TestCase):
    def test_rstrip_astrsk(self):
        # Test case where rstrip_astrsk is expected to modify the string, by removing trailing asterisks
        stripped = rstrip_astrsk('1.0**')
        self.assertEquals(stripped, '1.0')
        stripped = rstrip_astrsk('1.0*')
        self.assertEquals(stripped, '1.0')
        # Test case where rstrip_astrsk is not expected to modify string, bc asterisks are leading
        stripped = rstrip_astrsk('**1.0')
        self.assertEquals(stripped, '**1.0')
        # Test case where rstrip_astrsk is not expected to modify string, bc there are no asterisks
        stripped = rstrip_astrsk('1.0')
        self.assertEquals(stripped, '1.0')


if __name__=='__main__':
    unittest.main()