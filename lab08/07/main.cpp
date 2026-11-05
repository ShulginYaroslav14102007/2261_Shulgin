#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    
    vector<int> x(n);
    for (int &num : x) {
        cin >> num;
    }
    
    bool found = false;
    
    for (int num : x) {
        if (num < 0) {
            cout << num << endl;
            found = true;
            break;
        }
    }
    
    if (!found) {
        cout << "No negative numbers" << endl;
    }
    
    return 0;
}