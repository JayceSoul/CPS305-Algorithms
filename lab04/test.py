#Jonathan Ong
import unittest 
from mySolution import power, powerH, binoCo

class Test(unittest.TestCase):
    
    def test_power (self):
        t1 = power(2, 4, 1) #normal test
        t2 = power(2, 0, 1) #test case if n is zero
        t3 = power(0, 4, 1) #test case for if base is zero
        self.assertEqual(t1,16)
        self.assertEqual(t2,1)
        self.assertEqual(t3,0)
    
    def test_powerH (self):
        t1 = powerH(2, 4) #normal test
        t2 = powerH(2, 0) #test case if n is zero
        t3 = powerH(0, 4) #test case for if base is zero
        self.assertEqual(t1,16)
        self.assertEqual(t2,1)
        self.assertEqual(t3,0)
    
    
    def test_binoCo (self):
        t1 = binoCo(2,1) #normal test
        t2 = binoCo(2,0) #when k is 0
        t3 = binoCo(0,2) #when n is 0
        self.assertEqual(t1,2)
        self.assertEqual(t2,1)
        self.assertEqual(t3,0)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
