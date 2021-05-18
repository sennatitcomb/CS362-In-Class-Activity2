import unittest
import palindrome

class testCasePalindrome(unittest.TestCase):
    def test_1(self):
        result = palindrome.palindrome("butter")
        self.assertEqual(result,"This is not a palindrome")
    def test_2(self):
       result = palindrome.palindrome("racecar")
       self.assertEqual(result,"This is a palindrome")

if __name__ == '__main__':
    unittest.main();