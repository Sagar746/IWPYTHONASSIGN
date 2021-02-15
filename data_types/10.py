'''
10. Write a Python program to remove the characters which have odd index
values of a given string.
'''

def remove_odd_str(str):
	result=''

	for i in range(len(str)):
		if i%2==0:
			result=result+str[i]
	return result

print(remove_odd_str('Python'))
print(remove_odd_str('Sagar Tiwari'))