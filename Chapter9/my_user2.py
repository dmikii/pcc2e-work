from usermodule import User
from privadmin import Privileges, Admin

my_admin = Admin('Ouiki', 'Jones', 'Manager', 'Devtech', 'Sirius')

my_admin.privileges.show_privileges()