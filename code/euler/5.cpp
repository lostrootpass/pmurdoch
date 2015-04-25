/**
Problem five

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers from 1 to 20?
**/

#include <iostream>
#include <stdio.h>

int total = 2520;
int value = 0;

bool check( int what )
{
	for( int i = 11; i <= 20; i++ )
	{
		if( !(what % i == 0) )
		{
			return false;
		}
	}

	return true;
}

int main()
{
	for(int lol = 2520; ; lol += 2520 )
	{
		if( check( lol ) )
		{
			value = lol;
			break;
		}
	}

	std::cout << "Value is " << value << ".\n";
}
