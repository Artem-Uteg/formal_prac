from main import contains_word
import unittest

# Покрытие тестами 97%

class test_correct_regex(unittest.TestCase):
    def test(self):
        with self.assertRaises(ValueError) as context:
            contains_word("abd", 7, 3)
        self.assertTrue("regex invalid" in str(context.exception))
 
        with self.assertRaises(ValueError) as context:
            contains_word("+aaa", 7, 3)
        self.assertTrue("regex invalid" in str(context.exception))
 
        with self.assertRaises(ValueError) as context:
            contains_word("a+++", 7, 3)
        self.assertTrue("regex invalid" in str(context.exception))
 
        with self.assertRaises(ValueError) as context:
            contains_word("+", 7, 3)
        self.assertTrue("regex invalid" in str(context.exception))
    
        with self.assertRaises(ValueError) as context:
            contains_word("aa", 7, 3)
        self.assertTrue("regex invalid" in str(context.exception))

        with self.assertRaises(ValueError) as context:
            contains_word("a*", 4, 7)
        self.assertTrue("module or remain invalid" in str(context.exception))

        with self.assertRaises(ValueError) as context:
            contains_word("a*", 7, -1)
        self.assertTrue("module or remain invalid" in str(context.exception))

        with self.assertRaises(ValueError) as context:
            contains_word("a*", 0, 1)
        self.assertTrue("module or remain invalid" in str(context.exception))
 

class TestCorrectWork(unittest.TestCase):
    def test(self):
        assert contains_word('ab.*', 8, 5) == False
        assert contains_word('a', 12, 1) == True
        assert contains_word('ab.*', 12, 5) == False
        assert contains_word('abc.+*', 7, 5) == True
        assert contains_word('abccac.++.+*', 7, 4) == True
        assert contains_word('aabac....', 2, 1) == True
        assert contains_word('11+*', 6, 5) == False
 

if __name__ == '__main__':
    unittest.main()
