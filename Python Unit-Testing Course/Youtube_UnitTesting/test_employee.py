import unittest
from unittest.mock import patch
from employee import Employee

#tests don't always run in order. That's why you want to keep your tests isolated from one another

class TestEmployee(unittest.TestCase):

	#Do once at the beginning of the tests
	@classmethod
	def setUpClass(cls):
		print('setupClass')

	#Do once at the end of the tests
	@classmethod
	def tearDownClass(cls):
		print('teardownClass')

	#This code will run before every single test
	def setUp(self):
		print('setUp')
		#Have to be instance attributes so other tests can access them
		self.emp_1 = Employee('Corey', 'Schafer', 50000)
		self.emp_2 = Employee('Sue', 'Smith', 60000)
		

	#This code will run after every single test
	#i.e. delete a folder after testing
	def tearDown(self):
		print('tearDown\n')
		pass

	def test_email(self):
		print('test_email')
		self.assertEqual(self.emp_1.email, 'Corey.Schafer@email.com')
		self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')

		self.emp_1.first ='John'
		self.emp_2.first = 'Jane'

		self.assertEqual(self.emp_1.email, 'John.Schafer@email.com')
		self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')

	def test_fullname(self):
		print('test_fullname')
		self.assertEqual(self.emp_1.fullname, 'Corey Schafer')
		self.assertEqual(self.emp_2.fullname, 'Sue Smith')

		self.emp_1.first ='John'
		self.emp_2.first = 'Jane'
		
		self.assertEqual(self.emp_1.fullname, 'John Schafer')
		self.assertEqual(self.emp_2.fullname, 'Jane Smith')

	def test_applyRaise(self):
		print('test_applyRaise')
		self.emp_1.apply_raise()
		self.emp_2.apply_raise()
		
		self.assertEqual(self.emp_1.pay, 50000*1.05)
		self.assertEqual(self.emp_2.pay, 60000*1.05)

	def test_monthly_schedule(self):
		#Use patch as a context manager
		with patch('employee.requests.get') as mocked_get:
			mocked_get.return_value.ok = True
			mocked_get.return_value.text = 'Success'

			schedule = self.emp_1.monthly_schedule('May')
			mocked_get.assert_called_with('http://company.com/Schafer/May')
			self.assertEqual(schedule, 'Success')

			mocked_get.return_value.ok = False

			schedule = self.emp_2.monthly_schedule('June')
			mocked_get.assert_called_with('http://company.com/Smith/June')
			self.assertEqual(schedule, 'Bad Response!')


if __name__ == '__main__':
	unittest.main()