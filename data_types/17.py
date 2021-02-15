'''
Write a Python program to multiplies all the items in a list.
'''

from functools import reduce

alist=[1,2,3,4,5]
print(reduce(lambda a,b:a*b,alist))