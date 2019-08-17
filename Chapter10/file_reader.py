with open('pi_digits.txt') as file_object: # with keyword closes the file when it's no longer needed.
	contents = file_object.read()
print(contents)

# To open using a relative file path:
# with open('subfolder_of_current_folder/filename.txt') as file_object:

# To open with an absolute file path, assign it to a variable first:
# file_path = '/home/user/folder/subfolder/filenames.txt'
# with open(file_path) as file_object: