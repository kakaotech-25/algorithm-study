#include <bits/stdc++.h>
using namespace std;

int n, cnt1, cnt2;
int arr[41];

int fib(int k) {
    if(k == 1 || k == 2) {
        cnt1++;
        return 1;
    } else {
        return fib(n-1) + fib(n-2);
    }
}

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> n;
    fib(n);
    
    arr[1] = arr[2] = 1;

    for(int i=3; i<=3; i++) {
        arr[i] = arr[i-1] + arr[i-2];
        cnt2++;
    }
    
    cout << cnt1 << " " << cnt2;

    return 0;
}