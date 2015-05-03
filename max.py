def max2(a,b):
	if a > b:
		return a
	else:
		return b
def max3(a,b,c):
	if a>max2(b,c):
		return a
	else:
		return max2(b,c)
def max4(a,b,c,d):
	if max2(a,b)>max2(c,d):
		return max2(a,b)
	else:
		return max2(c,d)
def max5(a,b,c,d,e):
	if max2(a,b)>max3(c,d,e):
		return max2(a,b)
	else:
		return max3(c,d,e)
