'''

Write a Python program to remove duplicates from a list.
'''

a=[1,2,3,4,5,6,2,4,6]
b=dict.fromkeys(a)
print(list(b))