def answer(digits):
	return min(len(digits)//11,  digits.count('8'))

digits='801234567890123456789012345671234567'
print (answer(digits))