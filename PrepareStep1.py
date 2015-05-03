import StToFl

file1 = open('Auxiliary.txt', 'r')
file2 = open('Norm.txt', 'r')
file3 = open('LeftStep1.txt', 'w')
file4 = open('RightStep1.txt', 'w')
line = file1.readlines()[0]
m = StToFl.StToFloat(line) # a_ij

for i in file2:
	q = StToFl.StToFloat(i)
	b1  = q[1]*m[0]-q[0]*m[1]
	b2  = q[2]*m[1]-q[1]*m[2]
	b3  = q[3]*m[2]-q[2]*m[3]
	b4  = q[4]*m[3]-q[3]*m[4]
	b5  = q[5]*m[4]-q[4]*m[5]
	b6  = q[6]*m[5]-q[5]*m[6]
	b7  = q[7]*m[6]-q[6]*m[7]
	b8  = q[8]*m[7]-q[7]*m[8]
	b9  = q[9]*m[8]-q[8]*m[9]
	b10 = q[10]*m[9]-q[9]*m[10]
	b11 = q[11]*m[10]-q[10]*m[11]
	
	left = [[q[1],-q[0],0,0,0,0,0,0,0,0,0,0],[0,q[2],-q[1],0,0,0,0,0,0,0,0,0],[0,0,q[3],-q[2],0,0,0,0,0,0,0,0],[0,0,0,q[4],-q[3],0,0,0,0,0,0,0],[0,0,0,0,q[5],-q[4],0,0,0,0,0,0],[0,0,0,0,0,q[6],-q[5],0,0,0,0,0],[0,0,0,0,0,0,q[7],-q[6],0,0,0,0],[0,0,0,0,0,0,0,q[8],-q[7],0,0,0],[0,0,0,0,0,0,0,0,q[9],-q[8],0,0],[0,0,0,0,0,0,0,0,0,q[10],-q[9],0],[0,0,0,0,0,0,0,0,0,0,q[11],-q[10]],[q[0],q[1],q[2],q[3],q[4],q[5],q[6],q[7],q[8],q[9],q[10],q[11]]]
	right = [b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,80]
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
