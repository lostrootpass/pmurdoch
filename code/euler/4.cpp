#include <iostream>
#include <string>

long palindrome = 0;
int i = 999;
int j = 999;

bool isPal( long long i )
{
	long long temp = i;
	long long reverse = 0;

	while( temp > 0 )
	{
		reverse = (reverse * 10) + (temp%10);
		temp /= 10;
	}

	return (reverse == i) ? true : false;
}

int main()
{
	while( (i >= 100) && (palindrome == 0) )
	{
		while( (j >= 100) && (palindrome == 0) )
		{
			if( isPal( i * j ) )
				palindrome = (i * j);

			--j;
		}

		--i;
	}

	std::cout << "largest palindrome is: " << palindrome << "\n";
}
