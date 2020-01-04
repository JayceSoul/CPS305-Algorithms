
#Jonathan Ong
import unittest
from eval import evalTree, BinaryTree, getLeftChild, getRightChild,getRootVal,insertLeft,insertRight

class Test_mo3(unittest.TestCase):
    
#an expression with one number   
    def test_one (self):
        print("Test01 One Number")
        env = {
            'a':10,
            'b':20,
            'c':30
            }
        r = BinaryTree('a')
        print("Tree in list notation")
        print(r)
        res = evalTree(r,env)
        print(res)
        self.assertEqual(res, 10)
        print("\n")
        
#divide by zero        
    def test_zero (self):
        print("Test02 Divide by Zero")
        env = {
            'a':10,
            'b':30,
            'c':30
            }
        r = BinaryTree('/')
        insertLeft(r,'a')
        insertRight(r,'-')
        insertRight(getRightChild(r),'b')
        insertLeft(getRightChild(r),'c')
        print("Tree in list notation")
        print(r)
        res = evalTree(r,env)
        print(res)
        self.assertEqual(res, None)
        print("\n")

#testing for long expressions        
    def test_longexpression (self):
        print("Test03 Long expression")
        env = {
            'a':10,
            'b':20,
            'c':30,
            'd':40
            }
        r = BinaryTree('+')
        insertLeft(r,'a')
        insertRight(r,'*')
        insertRight(getRightChild(r),'-')
        insertLeft(getRightChild(r),'b')
        insertRight(getRightChild(getRightChild(r)), 'd')
        insertLeft(getRightChild(getRightChild(r)), 'c')
        print("Tree in list notation")
        print(r)
        res = evalTree(r,env)
        print(res)
        self.assertEqual(res, -190)
        print("\n")

#testing for missing a number in env        
    def test_missing (self):
        print("Test04 Missing")
        env = {
            'b':20,
            'c':30
            }
        r = BinaryTree('+')
        insertLeft(r,'a')
        insertRight(r,'b')
        print("Tree in list notation")
        print(r)
        res = evalTree(r,env)
        print(res)
        self.assertEqual(res, None)
        print("\n")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)