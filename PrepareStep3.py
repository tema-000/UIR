import StToFl

file1 = open('SolveStep1.txt', 'r')
file2 = open('SolveStep2.txt', 'r')
file3 = open('LeftStep3.txt', 'w')
file4 = open('RightStep3.txt', 'w')

line = file2.readlines()[0] 
m = StToFl.StToFloat(line) #xij с крышкой
print(m)

for i in file1:
	q = StToFl.StToFloat(i)
	b1 = q[0]-m[0]
	b2 = q[1]-m[1]
	b3 = q[2]-m[2]
	b4 = q[3]-m[3]
	b5 = q[4]-m[4]
	b6 = q[5]-m[5]
	b7 = q[6]-m[6]
	b8 = q[7]-m[7]
	b9 = q[8]-m[8]
	b10= q[9]-m[9]
	b11= q[10]-m[10]
	b12= q[11]-m[11]
	left = [[b2,b1,0,0,0,0,0,0,0,0,0,0],[0,b3,-b2,0,0,0,0,0,0,0,0,0],[0,0,b4,-b3,0,0,0,0,0,0,0,0],[0,0,0,b5,-b4,0,0,0,0,0,0,0],[0,0,0,0,b6,-b5,0,0,0,0,0,0],[0,0,0,0,0,b7,-b6,0,0,0,0,0],[0,0,0,0,0,0,b8,-b7,0,0,0,0],[0,0,0,0,0,0,0,b9,-b8,0,0,0],[0,0,0,0,0,0,0,0,b10,-b9,0,0],[0,0,0,0,0,0,0,0,0,b11,-b10,0],[0,0,0,0,0,0,0,0,0,0,b12,-b11],[1,1,1,1,1,1,1,1,1,1,1,1]]
	right = [[b2*m[0]-b1*m[1]],[b3*m[1]-b2*m[2]],[b4*m[2]-b3*m[3]],[b5*m[3]-b4*m[4]],[b6*m[4]-b5*m[5]],[b7*m[5]-b6*m[6]],[b8*m[6]-b7*m[7]],[b9*m[7]-b8*m[8]],[b10*m[8]-b9*m[9]],[b11*m[9]-b10*m[10]],[b12*m[10]-b11*m[11]],[320]]
	l = 0
	while l < 12:
		file3.write(str(left[l])+"\n")
		l = l + 1
	z = 0
	while z < 12:
		file4.write(str(right[z])+"\n")
		z = z + 1
file1.close()
file2.close()
file3.close()
file4.close()

