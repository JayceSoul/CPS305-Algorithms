from mySolution import infixToPostfixEval
import unittest
#Jonathan Ong

class Testscore(unittest.TestCase):

    #subtraction test    
    def test_subtration (self):
        value, equ = infixToPostfixEval("1 + 2 + 3")
        self.assertEqual(value,6)
        self.assertEqual(equ,"1 2 + 3 +")
    
    #addition test
    def test_addition (self):
        value, equ = infixToPostfixEval("6 - 2 - 1")
        self.assertEqual(value,3)
        self.assertEqual(equ,"6 2 - 1 -")
    
    #mutiplication test
    def test_mutiplication (self):
        value, equ = infixToPostfixEval("2 * 2 * 3")
        self.assertEqual(value,12)
        self.assertEqual(equ,"2 2 * 3 *")
    
    #division test
    def test_division (self):
        value, equ = infixToPostfixEval("6 / 2 / 3")
        self.assertEqual(value,1)
        self.assertEqual(equ,"6 2 / 3 /")

    #tests with all operations twice (in each case the factorial is used)  
    def test_all(self):
        value, equ = infixToPostfixEval("6 * ( ( ( 5 + 3 )  - 2 ) / 2 )")
        self.assertEqual(value,18)
        self.assertEqual(equ,"6 5 3 + 2 - 2 / *")
        value, equ = infixToPostfixEval("! 3  / ( 2 * 3 )")
        self.assertEqual(value,1)
        self.assertEqual(equ,"3 ! 2 3 * /")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)