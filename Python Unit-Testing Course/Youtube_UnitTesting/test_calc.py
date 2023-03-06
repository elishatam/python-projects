import unittest
import calc

#Run:
# 1) typing in command prompt: python -m unittest test_calc.py
# 2) python test_calc.py bc I have unittest.main()

class TestCalc(unittest.TestCase): #Inherit from unittest.TestCase

	def test_add(self):
		self.assertEqual(calc.add(10,5), 15)
		self.assertEqual(calc.add(-1,1), 0) #test edge case
		self.assertEqual(calc.add(-1,-1), -2)

	def test_subtract(self):
		self.assertEqual(calc.subtract(10,5), 5)
		self.assertEqual(calc.subtract(-1,1), -2) 
		self.assertEqual(calc.subtract(-1,-1), 0)

	def test_multiply(self):
		self.assertEqual(calc.multiply(10,5), 50)
		self.assertEqual(calc.multiply(-1,1), -1) 
		self.assertEqual(calc.multiply(-1,-1), 1)

	def test_divide(self):
		self.assertEqual(calc.divide(10,5), 2)
		self.assertEqual(calc.divide(-1,1), -1) 
		self.assertEqual(calc.divide(-1,-1), 1)			
		self.assertEqual(calc.divide(5,2), 2.5)

		#Test that exception was properly raised
		#Method 1: 
		#self.assertRaises(ValueError, calc.divide, 10, 0)

		#Method 2: Test with context manager. Will call function normally
		with self.assertRaises(ValueError):
			calc.divide(10,0)

if __name__ == '__main__':
	unittest.main()