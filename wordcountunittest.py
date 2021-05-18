import unittest
import wordcount

class testCaseWordCount(unittest.TestCase):
    def test_1(self):
        result = wordcount.wordcount("jam jelly")
        self.assertEqual(result, 2)
    def test_2(self):
       result = wordcount.wordcount("lego")
       self.assertEqual(result, 1)
    def test_3(self):
       result = wordcount.wordcount("blue red green")
       self.assertEqual(result, 3)
    def test_4(self):
       result = wordcount.wordcount(1400)
       self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main();