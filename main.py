import time
import random
import khi 
import genmat
import norm


start = time.time()
file1 = open("Khi.txt", 'w')
file2 = open("Norm.txt", 'w')
file3 = open("Auxiliary.txt", 'w')
s = []
finish = []
finish2 = []
i = 0
while i < 300:
	a = random.randint(1 , 4)
	s.append(a)
	i = i + 1
m = []
i = 0
while i < 300:
	m.append(s[i])
	i = i + 1
#file3.write(str(s)) #output begin sequen
r1 = genmat.genmat(s)
m1 = norm.norm(r1, 300.0)
file3.write(str(m1)+"\n")
l = []
random.shuffle(s)
i = 0
while i < 300:
	l.append(s[i])
	i = i + 1
r2 = genmat.genmat(l)
m2 = norm.norm(r2,300.0)
file3.write("\n"+str(l))
file3.write("\n"+str(r2))
file2.write("\n"+str(m2))
param = 0.0
param = khi.khi2(r1, r2)
file3.write("\n"+str(param))
if param < 18.0:
	finish.append(r2)
length = len(finish)
print(length)
p = 0
while p < 100000:
	u = 0
	r3 = []
	pi = 0
	normal = []
	while u < len(finish):
		q = []
		random.shuffle(s)
		y = 0
		while y < 300:
			q.append(s[y])
			y = y + 1
		r3 = genmat.genmat(q)
		r2 = finish[u]
		param = khi.khi2(r2, r3)
		file1.write("Khi = " + str(param)+"\n")
		if param < 19.4:
			pi = pi + 1
		else:
			break
		u = u + 1
	if pi >= len(finish):
		finish.append(r3)
		m3 = norm.norm(r3, 300.0)
		file2.write(str(m3)+"\n")
		file1.write("\n"+"++")
	else:
		file1.write("\n"+"--")
	if p%100 == 0:
		print(p)
	p = p + 1
fin = time.time()
print(fin-start)
print(len(finish))
file1.close()
file2.close()
file3.close()
