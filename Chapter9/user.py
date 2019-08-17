class User:
	"""Modelling a user."""
	def __init__(self, first_name, last_name, job_title, company, location):
		self.first_name = first_name
		self.last_name = last_name
		self.job_title = job_title
		self.company = company
		self.location = location
		self.login_attempts = 0

	def describe_user(self):
		print(f"{self.first_name} {self.last_name} is a {self.job_title} who works at {self.company} in {self.location}.")

	def greet_user(self):
		print(f"Hello {self.first_name}!")

	def increment_login_attempts(self, attempts):
		self.login_attempts += attempts

	def reset_login_attempts(self, attempts):
		self.login_attempts = 0

user_1 = User('Blee', 'Blokey', 'Manager', 'Skwipit', 'Mars')
user_2 = User('Fred', 'Smith', 'Technician', 'Techtech', 'Techavia')
user_3 = User('Jeannie', 'Sangfroid', 'CEO', 'Supremitas', 'The Moon')

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()

user_3.describe_user()
user_3.greet_user()

user_4 = User('Jake', 'Rakely', 'President', 'Joraka', 'Venus')

user_4.increment_login_attempts(1)
print(user_4.login_attempts)

user_4.increment_login_attempts(1)
print(user_4.login_attempts)

user_4.increment_login_attempts(1)
print(user_4.login_attempts)

user_4.reset_login_attempts(3)
print(user_4.login_attempts)