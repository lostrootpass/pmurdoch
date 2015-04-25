#include <iostream>
#include <stdio.h>

int total = 0;
int currentTerm = 1;
int previousTerm = 1;
int recentTerm = 1;

int main()
{
	while( currentTerm <= 4000000 )
	{
		currentTerm = previousTerm + recentTerm;
		recentTerm = previousTerm;
		previousTerm = currentTerm;

		if( !(currentTerm % 2) )
		{
			total += currentTerm;
		}
	}

	std::cout << "The answer is: " << total << "\n";
}
