#include <iostream>

long long number = 600851475143;
long long current = 2;
long long pos = 2;

int main()
{
	while( pos < number )
	{
		if( number % current == 0 )
		{
			number /= current;
		}
		else
		{
			++current;
		}

		++pos;
	}

	std::cout << "Largest prime factor is: " << number << "\n";
}
