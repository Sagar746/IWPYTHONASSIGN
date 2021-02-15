def string_both_ends(str1):
	if len(str1)<2:
		return ''
	return str1[0:2] + str1[-2:]

print(string_both_ends('Python'))
print(string_both_ends('Py'))
print(string_both_ends('w'))