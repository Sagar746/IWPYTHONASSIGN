'''
7. Write a Python function that takes a list of words and returns the length of the
longest one.

'''

def long_words(str1):
	word_len=[]
	for n in str1:
		word_len.append((len(n),n))
	return max(word_len)
		
		
print(long_words(['Laptop','Computer','Education']))