import unittest
import pandas as pd
from kata_three_shared import *

class Tests(unittest.TestCase):
    # Testing that the get_answer method is flexible, working with strings/floats, and negative numbers.
    # Also validating that the returned answer is what I expect
    def test_get_answer(self):
        table = pd.DataFrame([['loser1', '20.0', '22'],
                              ['loser2', '-10', '20.1'],
                              ['winner!', '20.0', 20.01],
                              ['loser3', 20.01, 20]],
                              columns=['name','low','high'])
        self.assertEqual(get_answer('low', 'high', table, 'name'), 'winner!')


if __name__=='__main__':
    unittest.main()