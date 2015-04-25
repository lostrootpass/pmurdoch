#include <iostream>
#include <stdio.h>

int squareTotal = 0;
int sumTotal = 0;

int main()
{
	for( int i = 1; i <= 100; i++ )
	{
		squareTotal += (i*i);
	}

	for( int i = 1; i <= 100; i++ )
	{
		sumTotal += i;
	}

	sumTotal = (sumTotal * sumTotal );

	std::cout << "Square of the sum: " << sumTotal << "\n";
	std::cout<< "Sum of squares: " << squareTotal << "\n";
	std::cout << "Difference: " << (squareTotal - sumTotal) << "\n";
}
