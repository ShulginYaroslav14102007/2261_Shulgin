#include <iostream>
using namespace std;

int main() {
    int from = 1;
    int to = 5;
    
    int __i = from, __n = to;
    for(const int &i=__i; i < __n; __i++) {
        cout << i << " ";
    }
    cout << endl;
    return 0;
}