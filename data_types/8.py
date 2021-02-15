'''
8. Write a Python program to remove the n
th
index character from a nonempty
string

'''

def remove_char(str,n):
	first_part=str[:n]
	second_part=str[n+1:]
	return first_part + second_part

print(remove_char('Python',0))
print(remove_char('Python',3))
print(remove_char('Python',5))