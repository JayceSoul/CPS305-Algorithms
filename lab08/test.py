
#Jonathan Ong
import unittest
from parse import parse, parseHelper, precedence, handleOp, numberp, operatorp

class Test_par(unittest.TestCase):
    
#an expression with empty expression   
    def test_None (self):
        print("Test01 empty expression")
        x = []
        print("Expression in list")
        print(x)
        self.assertEqual(parse(x), None)
        print("Expression after parsing")
        print("--", parse(x))
        print("\n")
        
#test for one number expressions  
    def test_one (self):
        print("Test02 One Number expressions")
        x=['2']
        print("Expression in list")
        print(x)
        self.assertEqual(parse(x), ['2', [], []])
        print("Expression after parsing")
        print("--", parse(x))
        print("\n")

#testing for factorial expressions        
    def test_factorial (self):
        print("Test03 factorial expressions")
        x = ['2', '!']
        print("Expression in list")
        print(x)
        self.assertEqual(parse(x), ['!', ['2', [], []], []])
        print("Expression after parsing")
        print("--", parse(x))
        print("\n")

#testing for expressions with parentheses      
    def test_para (self):
        print("Test04 expressions with parentheses")
        x = [['4', '+', '3'], '*', '7']
        print("Expression in list")
        print(x)
        self.assertEqual(parse(x), 	['*', ['+', ['4', [], []], ['3', [], []]], ['7', [], []]])
        print("Expression after parsing")
        print("--", parse(x))
        print("\n")


#testing with a long expression        
    def test_long (self):
        print("Test05 long expression")
        x = ['3','/',['6', '!'],'-', '9']
        print("Expression in list")
        print(x)
        self.assertEqual(parse(x), ['-', ['/', ['3', [], []], ['!', ['6', [], []], []]], ['9', [], []]])
        print("Expression after parsing")
        print("--", parse(x))
        print("\n")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)