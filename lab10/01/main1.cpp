#include <iostream>
using namespace std;

int main(){
 int a=10, b=20;
int *p=&a, *q=&b;

p=q;

cout<<*p<<" "<<*q <<endl;
cout<<p<<" "<<q <<" "<<a<< " "<<b<<endl;

return 0;
}