import unittest
from rabin_karp import search_pattern


class MyTestCase(unittest.TestCase):
    def test_from_task(self):
        self.assertEqual(search_pattern("101", "10101010101", 131, 256),
                         [('0', '2'), ('2', '4'), ('4', '6'), ('6', '8'), ('8', '10')])
        self.assertEqual(search_pattern("ok1", "ok i okalove NYXZC", 131, 256), [])
        self.assertEqual(search_pattern("Rick", "adaDSsRickFkeHca", 131, 256), [('6', '9')])
        self.assertEqual(search_pattern("Світло", "Світла Світлина Світить Світлом Світлані", 131, 256), [('24', '29')])