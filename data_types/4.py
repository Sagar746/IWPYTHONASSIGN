'''

4. Write a Python program to get a single string from two given strings, separated
by a space and swap the first two characters of each string.

'''

def swap_char(a,b):
	new_a=b[:2] + a[2:]
	new_b=a[:2] + b[2:]

	return new_a + ' ' + new_b
print(swap_char('abc','xyz'))