class Employee:
	def __init__(self,first_name,last_name,annual_salary='5000$'):
		
		self.first_name=first_name
		self.last_name=last_name
		self.annual_salary=annual_salary
		self.employee=f"{self.first_name} {self.last_name} {self.annual_salary}"


	def give_raise(self):
		

		print(f"{self.first_name} {self.last_name} have been given {self.annual_salary} of annual salary!")



