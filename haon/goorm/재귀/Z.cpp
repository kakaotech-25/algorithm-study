#include <bits/stdc++.h>
using namespace std;

int func(int n, int r, int c) {
    if(n == 1) {
        return 1;
    }

    int half = n/2;

    if(r < half && c < half) {
        return func(half, r, c);
    }

    else if(r < half && c >= half) {
        return half*half + func(half, r, c-half);
    }

    else if(r >= half && c < half) {
        return 2*half*half + func(half, r-half, c);
    }

    return 3*half*half + func(half, r-half, c-half);
}

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n, r, c;
    cin >> n >> r >> c;

    n = (1 << n);

    cout << func(n, r, c) - 1;

    return 0;
}