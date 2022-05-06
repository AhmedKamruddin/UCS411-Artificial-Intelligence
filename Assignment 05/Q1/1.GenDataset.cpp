#include <iostream>
#include <stdlib.h>
using namespace std;
int main( )
{
    int  exp, written, interview, salary;
    srand(time(0));
    for(int i = 1; i <= 25; i++)
    {
        exp=rand()%10;
        written=rand()%10;
        interview=rand()%10;
        salary=rand()%10000;
        cout<<exp<<", "<<written<<", "<<interview<<", "<<salary<<endl;
    }
}