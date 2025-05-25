import unittest
from employee import Employee

class TestCaseEmployee(unittest.TestCase):

	def setUp(self):
		self.first_name='Adrian'
		self.last_name='Casaysay'
		self.annual_salary='7500$'

		self.my_employee=Employee(self.first_name,self.last_name)
		self.my_employee_custom=Employee(self.first_name,self.last_name,self.annual_salary)

		
		

	



	def test_give_default_raise(self):
		
		self.assertEqual(f"Adrian Casaysay 5000$",self.my_employee.employee)
		

	def test_give_custom_raise(self):

		self.assertEqual(f"Adrian Casaysay 7500$",self.my_employee_custom.employee)
		

if __name__ == '__main__':
	unittest.main()





