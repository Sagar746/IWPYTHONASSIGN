'''
9. Write a Python program to change a given string to a new string where the first
and last chars have been exchanged.
'''

def change_string(str):
	return str[-1:] + str[1:-1] + str[:1]

print(change_string('ABCD'))
print(change_string('WXYZ'))