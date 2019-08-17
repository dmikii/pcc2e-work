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

class Privileges:
	"""Describing a class for privileges allowed on an account."""
	def __init__(self):
		self.privileges = ['can add a post', 'can delete a post', 'can ban a user']

	def show_privileges(self):
		for privilege in self.privileges:
			print(f"You {privilege}.")

class Admin(User):
	"""Describing attributes of an admin."""
	def __init__(self, first_name, last_name, job_title, company, location):
		super().__init__(first_name, last_name, job_title, company, location)
		self.privileges = Privileges()


my_admin_account = Admin('Blee', 'Blah', 'Janitor', 'Freeco', 'Prisonia')
# my_admin_account.show_privileges()
my_admin_account.greet_user()

my_admin_account.privileges.show_privileges()
