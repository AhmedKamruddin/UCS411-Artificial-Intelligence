#include <iostream>
#include <stdlib.h>
using namespace std;
int main( )
{
    int  gradPercent, exp, written, interview, selection;
    srand(time(0));
    for(int i = 1; i <= 25; i++)
    {
        gradPercent=rand()%100;
        exp=rand()%15;
        written=rand()%10;
        interview=rand()%10;
        selection=rand()%2;
        cout<<gradPercent<<", "<<exp<<", "<<written<<", "<<interview<<", "<<selection<<endl;
    }
}