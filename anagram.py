a = raw_input ('enter the 1st word ')
a1 = list(a)
b = raw_input ('enter the second word ')
b1 = list (b)
a1.sort()
b1.sort()
if a1 == b1:
	print 'anagram'
else:
	print 'not'
