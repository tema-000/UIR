import StToFl

file1 = open('Auxiliary.txt', 'r')
file2 = open('Norm.txt', 'r')
file3 = open('LeftStep2.txt', 'w')
file4 = open('RightStep2.txt', 'w')
line  = file1.readlines()[0]
m = StToFl.StToFloat(line)
left = [[m[1],-m[0],0,0,0,0,0,0,0,0,0,0],[0,m[2],-m[1],0,0,0,0,0,0,0,0,0],[0,0,m[3],-m[2],0,0,0,0,0,0,0,0],[0,0,0,m[4],-m[3],0,0,0,0,0,0,0],[0,0,0,0,m[5],-m[4],0,0,0,0,0,0],[0,0,0,0,0,m[6],-m[5],0,0,0,0,0],[0,0,0,0,0,0,m[7],-m[6],0,0,0,0],[0,0,0,0,0,0,0,m[8],-m[7],0,0,0],[0,0,0,0,0,0,0,0,m[9],-m[8],0,0],[0,0,0,0,0,0,0,0,0,m[10],-m[9],0],[0,0,0,0,0,0,0,0,0,0,m[11],-m[10]],[m[0],m[1],m[2],m[3],m[4],m[5],m[6],m[7],m[8],m[9],m[10],m[11]]]
right = [0,0,0,0,0,0,0,0,0,0,0,80]
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
		