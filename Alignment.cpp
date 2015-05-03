// Alignment.cpp: определяет точку входа для консольного приложения.
//

#include <iostream>
#include <string>
#include <memory.h>
#include <cstdlib>
#include <math.h>
#include <iomanip>
#include <stdlib.h>
#include <fstream>
#include <sstream>
#include "time.h"
#include <ctime>
#include <vector>
#include <algorithm>
#include <iterator>
 

using namespace std;

float max2(float a, float b)
{
	if (a > b)
		return a;
	else
		return b;
}

float max3(float a, float b, float c)
{
	if (a > max2(b, c))
		return a;
	else
		return max2(b, c);
}

float max5(float a, float b, float c, float d, float e)
{
	if (max2(a, b) > max3(c, d, e))
		return max2(a, b);
	else
		return max3(c, d, e);
}
float max4(float a, float b, float c, float d)
{
	if (max2(a, b) > max2(c, d))
		return max2(a, b);
	else
		return max2(c, d);
}
int main()
{
	float delta = 100000000.0;
	float q = 3.0;
	float p;
	int a,b,c,d,e,f,g,h,val;
	float array[300][300];
	float array2[300][300];
	float arr[300][300];
	float arr2[300][300];
	float FS = 0.0;
	float mat[3][4] = { { 3.464637746, -0.25591837, -4.181568998, 0.872045521 }, { 4.355807327, -15.35845639, 3.810040260, 7.304450524 }, { -5.119475256, 10.84788064, 3.250390199, -9.618086422 } };
	float inv[3][4] = { { 10.84788064, -5.119475256, -9.618086422, 3.250390199 }, { -15.35845639, 4.355807327, 7.304450524, 3.810040260 }, { -0.25591837, 3.464637746, 0.872045521, -4.181568998 } };
	float sequen[301] = {0, 2, 1, 2, 3, 1, 2, 4, 3, 3, 1, 2, 2, 3, 2, 4, 4, 4, 3, 1, 4, 3, 1, 1, 2, 3, 4, 2, 1, 2, 4, 2, 1, 3, 4, 3, 1, 4, 1, 2, 3, 2, 1, 3, 2, 2, 4, 3, 2, 3, 3, 1, 4, 1, 1, 2, 3, 4, 3, 3, 3, 2, 1, 3, 4, 2, 4, 4, 2, 3, 3, 1, 3, 3, 3, 4, 1, 2, 3, 2, 2, 3, 4, 1, 3, 1, 1, 3, 1, 3, 2, 4, 3, 1, 4, 4, 2, 4, 3, 3, 3, 4, 2, 2, 3, 2, 1, 3, 1, 3, 2, 3, 1, 3, 1, 3, 1, 2, 4, 1, 4, 3, 4, 4, 4, 1, 2, 3, 1, 1, 2, 1, 4, 2, 4, 1, 3, 1, 1, 1, 1, 3, 2, 4, 1, 1, 3, 4, 4, 4, 2, 4, 3, 1, 2, 2, 1, 3, 2, 4, 1, 3, 1, 4, 3, 2, 4, 3, 3, 1, 3, 4, 4, 3, 4, 3, 3, 1, 3, 1, 3, 2, 1, 2, 1, 1, 1, 4, 2, 3, 1, 4, 2, 3, 1, 2, 2, 2, 3, 3, 2, 4, 2, 2, 2, 4, 3, 4, 4, 1, 1, 3, 2, 4, 3, 2, 2, 1, 1, 2, 4, 2, 3, 3, 4, 3, 4, 4, 2, 1, 4, 2, 4, 2, 3, 1, 3, 2, 1, 2, 2, 2, 3, 4, 1, 3, 3, 3, 1, 4, 4, 1, 4, 3, 2, 2, 3, 1, 4, 3, 3, 2, 1, 2, 3, 4, 3, 3, 1, 4, 4, 2, 4, 4, 4, 1, 3, 4, 2, 3, 2, 2, 4, 4, 2, 1, 2, 2, 3, 1, 3, 2, 4, 1, 2, 1, 2, 4, 3, 1, 2 };
	float a1 = mat[0][0], t1 = mat[0][1], c1 = mat[0][2], g1 = mat[0][3];
	float a2 = mat[1][0], t2 = mat[1][1], c2 = mat[1][2], g2 = mat[1][3];
	float a3 = mat[2][0], t3 = mat[2][1], c3 = mat[2][2], g3 = mat[2][3];
	float ia1 = inv[0][0], it1 = inv[0][1], ic1 = inv[0][2], ig1 = inv[0][3];
	float ia2 = inv[1][0], it2 = inv[1][1], ic2 = inv[1][2], ig2 = inv[1][3];
	float ia3 = inv[2][0], it3 = inv[2][1], ic3 = inv[2][2], ig3 = inv[2][3];
	for (int i = 0; i < 300; i++)
	{
		array[0][i]  = 0;
		array2[0][i] = 0;
		array[i][0]  = 0;
		array2[i][0] = 0;
		arr[0][i]=0;
		arr[i][0] = 0;
		arr2[0][i]=0;
		arr2[i][0]=0;
	}
	for (int i = 1; i < 300; i++) //строка по последовательности
	{
		for (int j = 1; j < 300; j++) //столбец по матрице
		{
			a = array[i - 1][j] - q;
			b = array[i][j - 1] - q;
			c = array2[i - 1][j - 1]-delta;
			d = array2[i][j - 1] + q;
			e = array2[i - 1][j] + q;
			f = array[i - 1][j - 1] + delta;
			g = array[i - 1][j - 1];
			h = array2[i - 1][j - 1];
			val = sequen[j];
			if  (i%3==2)
			{
				switch (val)
				{
				case 1:
					p = max5(0, a, b, c, g + a1);
					array[i][j]  = p;
					if (p==0)
						arr[i][j] = 1;
					if (p == a)
						arr[i][j] = 2;
					if (p == b)
						arr[i][j] = 3;
					if (p == c)
						arr[i][j] = 4;
					if (p == g + a1)
						arr[i][j] = 5;
					array2[i][j] = max4(d, e, f, h + ia1);
					break;
				case 2:
					p = max5(0, a, b, c, g + t1);
					array[i][j]  = p;
					if (p==0)
						arr[i][j] = 1;
					if (p == a)
						arr[i][j] = 2;
					if (p == b)
						arr[i][j] = 3;
					if (p == c)
						arr[i][j] = 4;
					if (p == g + t1)
						arr[i][j] = 5;
					array2[i][j] = max4(d, e, f, h + it1);
					break;
				case 3:
					p = max5(0, a, b, c, g + c1);
					array[i][j]  = p;
					if (p==0)
						arr[i][j] = 1;
					if (p == a)
						arr[i][j] = 2;
					if (p == b)
						arr[i][j] = 3;
					if (p == c)
						arr[i][j] = 4;
					if (p == g + c1)
						arr[i][j] = 5;
					array2[i][j] = max4(d, e, f, h + ic1);
					break;
				default:
					p = max5(0, a, b, c, g + g1);
					array[i][j]  = p;
					if (p==0)
						arr[i][j] = 1;
					if (p == a)
						arr[i][j] = 2;
					if (p == b)
						arr[i][j] = 3;
					if (p == c)
						arr[i][j] = 4;
					if (p == g + g1)
						arr[i][j] = 5;
					array2[i][j] = max4(d, e, f, h + ig1);
				}
			}
			if (i % 3 == 1)
			{
				switch (val)
				{
				case 1:
					p = max5(0, a, b, c, g + a2);
					array[i][j]  = p;
					if (p==0)
						arr[i][j] = 1;
					if (p == a)
						arr[i][j] = 2;
					if (p == b)
						arr[i][j] = 3;
					if (p == c)
						arr[i][j] = 4;
					if (p == g + a2)
						arr[i][j] = 5;
					array2[i][j] = max4(d, e, f, h + ia2);
					break;
				case 2:
					p = max5(0, a, b, c, g + t2);
					array[i][j]  = p;
					if (p==0)
						arr[i][j] = 1;
					if (p == a)
						arr[i][j] = 2;
					if (p == b)
						arr[i][j] = 3;
					if (p == c)
						arr[i][j] = 4;
					if (p == g + t2)
						arr[i][j] = 5;
					array2[i][j] = max4(d, e, f, h + it2);
					break;
				case 3:
					p = max5(0, a, b, c, g + c2);
					array[i][j]  = p;
					if (p==0)
						arr[i][j] = 1;
					if (p == a)
						arr[i][j] = 2;
					if (p == b)
						arr[i][j] = 3;
					if (p == c)
						arr[i][j] = 4;
					if (p == g + c2)
						arr[i][j] = 5;
					array2[i][j] = max4(d, e, f, h + ic2);
					break;
				default:
					p = max5(0, a, b, c, g + g2);
					array[i][j]  = p;
					if (p==0)
						arr[i][j] = 1;
					if (p == a)
						arr[i][j] = 2;
					if (p == b)
						arr[i][j] = 3;
					if (p == c)
						arr[i][j] = 4;
					if (p == g + g2)
						arr[i][j] = 5;
					array2[i][j] = max4(d, e, f, h + ig2);
				}
			}
			if (i % 3 == 0)
			{
				switch (val)
				{
				case 1:
					p = max5(0, a, b, c, g + a3);
					array[i][j]  = p;
					if (p==0)
						arr[i][j] = 1;
					if (p == a)
						arr[i][j] = 2;
					if (p == b)
						arr[i][j] = 3;
					if (p == c)
						arr[i][j] = 4;
					if (p == g + a3)
						arr[i][j] = 5;
					array2[i][j] = max4(d, e, f, h + ia3);
					break;
				case 2:
					p = max5(0, a, b, c, g + t3);
					array[i][j]  = p;
					if (p==0)
						arr[i][j] = 1;
					if (p == a)
						arr[i][j] = 2;
					if (p == b)
						arr[i][j] = 3;
					if (p == c)
						arr[i][j] = 4;
					if (p == g + t3)
						arr[i][j] = 5;
					array2[i][j] = max4(d, e, f, h + it3);
					break;
				case 3:
					p = max5(0, a, b, c, g + c3);
					array[i][j]  = p;
					if (p==0)
						arr[i][j] = 1;
					if (p == a)
						arr[i][j] = 2;
					if (p == b)
						arr[i][j] = 3;
					if (p == c)
						arr[i][j] = 4;
					if (p == g + c3)
						arr[i][j] = 5;
					array2[i][j] = max4(d, e, f, h + ic3);
					break;
				default:
					p = max5(0, a, b, c, g + g3);
					array[i][j]  = p;
					if (p==0)
						arr[i][j] = 1;
					if (p == a)
						arr[i][j] = 2;
					if (p == b)
						arr[i][j] = 3;
					if (p == c)
						arr[i][j] = 4;
					if (p == g + g3)
						arr[i][j] = 5;
					array2[i][j] = max4(d, e, f, h + ig3);
				}
			}

		}

	}
	int count = 0;
	for (int i =0; i<300; i++)
	{
		for (int j = 0; j < 300; j++)
		{
			if (array[i][j] == 0)
				count++;
			cout<<array[i][j]<<endl;
		}
		cout << endl;
	}
	cout << count;
	return 0;
}
