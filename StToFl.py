def StToFloat(line):
	a = ""
	i = 0
	q = []
	while line[i]!=",":
		a = a + line[i]
		i = i + 1
	q.append(float(a))
		
	a = ""
	i = i + 2
	while line[i]!=",":
	
		a = a + line[i]
		i = i + 1
		
	q.append(float(a))
	a = ""
	i = i + 2
	while line[i]!=",":
		a = a + line[i]
		i = i + 1
	q.append(float(a))
	a = ""
	i = i + 2
	while line[i]!=",":
		a = a + line[i]
		i = i + 1
	q.append(float(a))
	a = ""
	i = i + 2
	while line[i]!=",":
		a = a + line[i]
		i = i + 1
	q.append(float(a))
	a = ""
	i = i + 2
	while line[i]!=",":
		a = a + line[i]
		i = i + 1
	q.append(float(a))
	a = ""
	i = i + 2
	while line[i]!=",":
		a = a + line[i]
		i = i + 1
	q.append(float(a))
	a = ""
	i = i + 2
	while line[i]!=",":
		a = a + line[i]
		i = i + 1
	q.append(float(a))
	a = ""
	i = i + 2
	while line[i]!=",":
		a = a + line[i]
		i = i + 1
	q.append(float(a))
	a = ""
	i = i + 2
	while line[i]!=",":
		a = a + line[i]
		i = i + 1
	q.append(float(a))
	a = ""
	i = i + 2
	while line[i]!=",":
		a = a + line[i]
		i = i + 1
	q.append(float(a))
	a = ""
	i = i + 2
	while line[i]!="\n":
		a = a + line[i]
		i = i + 1
	q.append(float(a))
	return q

	