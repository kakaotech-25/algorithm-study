#include <bits/stdc++.h>
using namespace std;

stack<char> s;

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    string str;
    cin >> str;
    
    for(int i=0; i<str.size()/2; i++) {
        s.push(str[i]);
    }

    bool isPalin = true;
    int mid = 0;

    if(str.size() % 2 == 1) {
        mid = str.size()/2 + 1;
    } else {
        mid = str.size()/2;
    }

    for(int i=mid; i<str.size(); i++) {
        if(s.top() == str[i]) {
            s.pop();
        } else {
            isPalin = false;
            break;
        }
    }

    if(isPalin) {
        cout << 1;
    } else {
        cout << 0;
    }

    return 0;
}