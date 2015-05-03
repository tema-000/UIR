	p = 1
	q = 0
	fopen('SolveStep1.txt', 'at+')
	while p <=1332
	L = dlmread('LeftStep1.txt', ',', [q*12 0 (p*12-1) 11]);
	N = dlmread('RightStep1.txt', ' ', [q*12 0 (p*12-1) 0]);
	C =rref([L N]);
	n = size(C);
	x = C(:,n(2));
	m = x';
	dlmwrite('SolveStep1.txt', m, "-append" );
	p = p + 1
	q = q + 1
end
	
