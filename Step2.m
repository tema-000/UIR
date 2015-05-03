L = dlmread('LeftStep2.txt', ',', [0 0 11 11])
N = dlmread('RightStep2.txt', ' ', [0 0 11 0])
C =rref([L N])
n = size(C)
x = C(:,n(2))
L*x-N
dlmwrite('SolveStep2.txt', m, "-append" );


	