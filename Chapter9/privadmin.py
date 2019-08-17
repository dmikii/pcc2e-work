class Privileges:
	"""Describing a class for privileges allowed on an account."""
	def __init__(self):
		self.privileges = ['can add a post', 'can delete a post', 'can ban a user']

	def show_privileges(self):
		for privilege in self.privileges:
			print(f"You {privilege}.")

class Admin:
	"""Describing attributes of an admin."""
	def __init__(self, first_name, last_name, job_title, company, location):
		# super().__init__(first_name, last_name, job_title, company, location)
		self.privileges = Privileges()

