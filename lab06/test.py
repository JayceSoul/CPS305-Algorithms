#Jonathan Ong
import unittest
from sorting import mo3_quicksort, quickSort


class Test_mo3(unittest.TestCase):
    
#normal list    
    def test_sort (self):
        data = [13,121,231,21,1,23,5]
        print("Before:")
        print(data)
        mo3_quicksort(data)
        self.assertEqual(data, [1,5,13,21,23,121,231])
        print("After:")
        print(data)
        
#when list is empty        
    def test_empty (self):
        data = []
        print("Before:")
        print(data)
        mo3_quicksort(data)
        self.assertEqual(data, [])
        print("After:")
        print(data)

#when enteries are all the same        
    def test_same (self):
        data = [1,1,1,1,1,1,]
        print("Before:")
        print(data)
        mo3_quicksort(data)
        self.assertEqual(data, [1,1,1,1,1,1])
        print("After:")
        print(data)

class Test_qs(unittest.TestCase):
#normal list
    def test_sort (self):
        data = [13,121,231,21,1,23,5]
        print("Before:")
        print(data)
        quickSort(data)
        self.assertEqual(data, [1,5,13,21,23,121,231])
        print("After:")
        print(data)
        
#when list is empty
    def test_empty (self):
        data = []
        print("Before:")
        print(data)
        quickSort(data)
        self.assertEqual(data, [])
        print("After:")
        print(data)
        
#when enteries are all the same
    def test_same (self):
        data = [1,1,1,1,1,1,]
        print("Before:")
        print(data)
        quickSort(data)
        self.assertEqual(data, [1,1,1,1,1,1])
        print("After:")
        print(data)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

