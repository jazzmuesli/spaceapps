import sys, os

sys.path.insert(0, os.path.dirname(__file__))

import unittest
from sentence_parser import parse
# run python sentence_parser_test.py
class TestSentenceParser(unittest.TestCase):
  def test_upper(self):
      self.assertEqual((['bring'],['spanner']), parse('bring me a spanner'))
if __name__ == '__main__':
    unittest.main()
