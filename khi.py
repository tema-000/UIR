def khi2(sec1, sec2):
	khi = 0.0
	m = 0
	while m < 12:
		khi = khi + ((sec1[m]-sec2[m])**2)/(sec1[m]+sec2[m])
		m = m+1
	return khi