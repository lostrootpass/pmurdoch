#include <iostream>

int primeCount = 6;
int currentPrime = 13;
int count = 13;
int test;

int main()
{
	while( primeCount != 10001 )
	{
		count++;

		for( test = 2; test < count; ++test )
		{
			if( count % test == 0 )
				break;

			if( test == (count - 1 ) )
				primeCount++, currentPrime = count;
		}
	}
	std::cout << "The 10001st prime is " << currentPrime << "\n";
}
