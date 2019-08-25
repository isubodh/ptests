import unittest
import mymath 
'''
Test using the command below swith for detailed output
python unit-test.py -v 
'''

class Test(unittest.TestCase):
	def test_isPrime(self):
		result = mymath.isPrime(-1) ; self.assertFalse(result)
		result = mymath.isPrime(0) ; self.assertTrue(result)
		result = mymath.isPrime(1) ; self.assertTrue(result)
		result = mymath.isPrime(2) ; self.assertTrue(result)
		result = mymath.isPrime(3) ; self.assertTrue(result)
		result = mymath.isPrime(5) ; self.assertTrue(result)
		result = mymath.isPrime(6) ; self.assertFalse(result)
		result = mymath.isPrime(20) ; self.assertFalse(result)
		result = mymath.isPrime(23) ; self.assertTrue(result)
		
	def test_isEven(self):
		result = mymath.isEven(0) ; self.assertTrue(result)
		result = mymath.isEven(2) ; self.assertTrue(result)
		result = mymath.isEven(10) ; self.assertTrue(result)
		result = mymath.isEven(200) ; self.assertTrue(result)
		result = mymath.isEven(1) ; self.assertFalse(result)
		result = mymath.isEven(3) ; self.assertFalse(result)
		result = mymath.isEven(99) ; self.assertFalse(result)
		result = mymath.isEven(199) ; self.assertFalse(result)
		
	def test_isOdd(self):
		result = mymath.isOdd(0) ; self.assertFalse(result)
		result = mymath.isOdd(2) ; self.assertFalse(result)
		result = mymath.isOdd(10) ; self.assertFalse(result)
		result = mymath.isOdd(200) ; self.assertFalse(result)
		result = mymath.isOdd(1) ; self.assertTrue(result)
		result = mymath.isOdd(3) ; self.assertTrue(result)
		result = mymath.isOdd(99) ; self.assertTrue(result)
		result = mymath.isOdd(199) ; self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()