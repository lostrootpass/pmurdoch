/**
Problem three: The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
**/

#include <iostream>
#include <stdio.h>

long long large = 600851475143;
long long count = 3;
long largestPrime = 3;

int main()
{
	while( count < large )
	{
		if( ( large / count ) == ( count || 1 ) )
		{
			largestPrime = count;
		}

		++count;
	}

	std::cout << "Largest prime factor is: " << largestPrime << "\n";
}
