#include <iostream>
using namespace std;

int main() {
    int a = 5, b = 3;
    int c = 10;
    
    int mult = a * b;
    
    int *p = &a; 
    
    *p = 15;
    
    int bitwise = c & b; 
    
    int &ref = c;
    ref = 20;
    
    cout << "a = " << a << endl;
    cout << "bitwise = " << bitwise << endl;
    cout << "c = " << c << endl;
    
    return 0;
}