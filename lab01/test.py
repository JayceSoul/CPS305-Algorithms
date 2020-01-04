import unittest
from mySolution import generate 
from mySolution import calculateScore


class Testgenerate(unittest.TestCase):
    
    def test_letters (self):
        data = generate(1)
        alpha = "abcdefghijklmnopqrstuvwxyz "
        self.assertIn(data, alpha)
        
    def test_length (self):
        self.assertEqual(len(generate(5)), 5)
    
class Testscore(unittest.TestCase):
    
    def test_equ100 (self):
        data = calculateScore("abcdefghij","abcdefghij")
        self.assertEqual(data,100.0)
    
    def test_equZero (self):
        data = calculateScore("1234567890","abcdefghij")
        self.assertEqual(data,0)
    


